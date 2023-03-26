import streamlit as st
import requests

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


def display_node_info(node_address, node_data):
    st.write('---')
    col1, col2, col3 = st.columns(3)
    col1.metric("Node Address", node_address[:4] + "...")
    col1.metric("Status", node_data['data']['node']['status'])
    col1.metric("Staked $DATA", node_data['data']['node']['staked'])
    col2.metric("To be Received", round(
        node_data['data']['node']['toBeReceived'], 2))
    col2.metric("Rewards", node_data['data']['node']['rewards'])
    col3.metric("Claim Count", node_data['data']['node']['claimCount'])
    col3.metric("Claim %", round(
        node_data['data']['node']['claimPercentage'], 2))


def display_node_story(node_address, node_data, metrics_data):
    st.write('---')
    st.header(f"Story of node {node_address[:4]}...{node_address[38:]} :tada:")
    st.write(
        f"The node with address {node_address} has accumulated {metrics_data['acc_rewards']['DATA']} DATA as rewards.")
    st.write(
        f"The node has claimed rewards {metrics_data['claimed_rewards']['claimCount']} times.")
    st.write(
        f"The first claim was on {node_data['data']['node']['firstClaim']['claimTime']}")
    st.write(
        f"The last claim was on {node_data['data']['node']['lastClaim']['claimTime']}")
    st.write(
        f"The node has a claim percentage of {node_data['data']['node']['claimPercentage']}")
    st.write(
        f"The 24-hour APR is {metrics_data['apr_apy']['24h-APR']} and the 24-hour APY is {metrics_data['apr_apy']['24h-APY']}")
    st.write(
        f"The amount of data staked in the last 24 hours is {metrics_data['apr_apy']['24h-data-staked']}")


def main():
    st.title("Streamr API Dashboard")
    with st.expander('Enter node address'):
        node_address = st.text_input(
            "", "0x4a2a3501e50759250828acd85e7450fb55a10a69")

    if node_address:
        node_data = fetch_node_data(node_address)
        metrics_data = get_metrics_data(node_address)
        display_node_info(node_address, node_data)
        display_node_story(node_address, node_data, metrics_data)


if __name__ == '__main__':
    main()
