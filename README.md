# ⚡Streamr BrubeckScan Dashboard App⚡
 
 ![App Demo](assets/app.webm)

The Streamr BrubeckScan Dashboard App is a Streamlit version clone of the original [BrubeckScan App](https://brubeckscan.app/) designed for fetching and visualizing detailed information about any Streamr node in the network. The application effectively interacts with the Streamr Network's [BrubeckScan API](https://brubeckscan.app/api) to retrieve the latest data about a node given its Ethereum address.

This makes it an essential tool for anyone interested in or working with the Streamr Network, including node operators.

## Deployed Streamlit App

Click to view 👇🏾

[![Streamr BrubeckScan Dashboard App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)][def]

[def]: https://streamr.streamlit.app/

## Features

- **Ethereum Address Input:** Simply input the Ethereum address of a Streamr node to start fetching data.
- **Detailed Node Information:** The application displays comprehensive information about a node including its status, staked $DATA, to be received rewards, total rewards, claim count, and claim percentage.
- **Reward Payouts and Reward Codes:** It also presents the reward payouts and the latest claimed reward codes in a well-organized, easy-to-read format.
- **Efficient Data Fetching:** The application employs multi-threading to fetch data, ensuring that all data is fetched in an efficient and timely manner.
- **User Timezone Selection:** Users can select their own timezone for the display of time-related information.

## Installation

To set up the Streamr BrubeckScan Dashboard App by replicating this project, follow the steps below:

1. **Python:** Ensure that you have Python 3.7 or later [installed](https://www.python.org/downloads/) on your machine.

2. **Clone the Repository:** Clone this repository to your local machine:

    ```bash
    git clone https://github.com/tonykipkemboi/StreamrDashboard.git
    ```

3. **Install Requirements:** Navigate to the cloned repository and install the necessary Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Running the Application**: To run the Streamlit app, use the command:

   ```bash
   streamlit run streamr_app.py
   ```

2. **Accessing the Dashboard**: Open your web browser and navigate to <http://localhost:8501> to interact with the app.

3. **Entering Node Address**: Enter the Ethereum address of the Streamr node for which you want to fetch and display data; `I provided an example for testing`!

4. **Viewing Data**: The fetched data will be displayed in an organized and user-friendly manner. You can also select your timezone for the display of time-related data.

With these steps, you can easily and efficiently _fetch_, _visualize_, and _analyze_ data for any Streamr node in the network.
