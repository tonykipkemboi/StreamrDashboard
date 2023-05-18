import streamlit as st
import requests
from datetime import datetime
import pytz
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image
import io
import math

API_BASE = "https://brubeckscan.app/api"


def fetch_data(endpoint):
    response = requests.get(endpoint)
    return response.json()


def fetch_node_data(node_address):
    return fetch_data(f"{API_BASE}/nodes/{node_address}")


def get_metrics_data(node_address):
    data = {
        "acc_rewards": f"https://brubeck1.streamr.network:3013/datarewards/{node_address}",
        "claimed_rewards": f"https://brubeck1.streamr.network:3013/stats/{node_address}",
        "apr_apy": "https://brubeck1.streamr.network:3013/apy"
    }
    return {k: fetch_data(v) for k, v in data.items()}


def check_status(status):
    return ":green[OK]" if status else ":red[NO]"


def display_node_info(node_address, node_data):
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.image(node_data['data']['node']['identiconURL'],
               caption='Node Identicon')
    col2.metric("Node Address", node_address[:4] + "...")
    col1.markdown(
        f"Status: **{check_status(node_data['data']['node']['status'])}**")
    col3.metric("Staked $DATA", node_data['data']['node']['staked'])
    col2.metric("To be Received", round(
        node_data['data']['node']['toBeReceived'], 2))
    col2.metric("Total rewards", node_data['data']['node']['rewards'])
    col3.metric("Claim Count", node_data['data']['node']['claimCount'])
    col3.metric("Percentage of received claims %", round(
        node_data['data']['node']['claimPercentage'], 2))


def display_latest_codes(node_data, col):
    all_timezones = pytz.all_timezones
    selected_tz = col.selectbox(
        "Select your timezone", all_timezones, index=all_timezones.index('US/Eastern'))
    user_tz = pytz.timezone(selected_tz)
    utc = pytz.timezone('UTC')

    for code in node_data['data']['node']['claimedRewardCodes']:
        # Convert the claimTime to a datetime object
        claim_time = datetime.strptime(
            code['claimTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
        # Set the timezone to UTC (since the original time is in UTC)
        claim_time = utc.localize(claim_time)
        # Convert to user selected timezone
        claim_time_user_tz = claim_time.astimezone(user_tz)
        # Format the time in the desired way (12-hour time)
        formatted_time = claim_time_user_tz.strftime("%I:%M:%S %p")
        col.write(f"{code['id']} → {formatted_time}")


def display_svg(col, path, width=None, height=None):
    # Load the SVG file and convert it to a ReportLab Drawing
    drawing = svg2rlg(path)

    # Convert the Drawing to a PIL image
    pil_image = renderPM.drawToPIL(drawing)

    # Resize the image if width and height are provided
    if width and height:
        pil_image = pil_image.resize((width, height))

    # Convert the PIL image to an IO Bytes object so Streamlit can display it
    image_stream = io.BytesIO()
    pil_image.save(image_stream, format='PNG')
    pil_image = Image.open(image_stream)

    # Display the image
    col.image(pil_image, use_column_width=False)


def display_payouts(node_data):
    # Create placeholders for headers
    st.divider()
    header1, header2 = st.columns(2)

    header1.header("Payouts")
    header2.header("Latest codes")

    # Create columns for the contents
    cols = st.columns([4, 2, 12])

    utc = pytz.timezone('UTC')
    payouts = node_data['data']['node']['payouts']
    payouts.reverse()
    for payout in payouts:
        # Convert the timestamp to a datetime object
        payout_time = datetime.utcfromtimestamp(int(payout['timestamp']))
        # Set the timezone to UTC
        payout_time = utc.localize(payout_time)
        # Format the time in the desired way
        formatted_time = payout_time.strftime("%a, %d %b %Y %H:%M:%S %Z")
        rounded_payout = math.ceil(float(payout['value']))

        # Use the first column for the text and the second for the SVG
        cols[0].markdown(f"{formatted_time} → {rounded_payout}")
        display_svg(cols[1], "assets/data_token.svg", width=20, height=20)

    # Display the latest codes in the third column
    display_latest_codes(node_data, cols[2])
    st.divider()


def main():
    st.title("⚡ Streamr BrubeckScan Dashboard ⚡")
    node_address = st.text_input(
        "Enter a Streamr node Ethereum address here", placeholder="0x4a2A3501e50759250828ACd85E7450fb55A10a69", max_chars=42)

    if node_address:
        node_data = fetch_node_data(node_address)
        get_metrics_data(node_address)
        display_node_info(node_address, node_data)
        display_payouts(node_data)


if __name__ == '__main__':
    main()
