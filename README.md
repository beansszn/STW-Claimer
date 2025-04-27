# Fortnite Node Claiming Script

This script automates the process of claiming various nodes in Fortnite Save the World (STW). It uses asynchronous HTTP requests to interact with the Epic Games API and claim nodes in bulk. The script tracks the success and failure of each claim operation, and provides a visual summary of the process using the `rich` library.

## Features

- Claims nodes in Fortnite Save the World using the Epic Games API.
- Tracks and displays successful and failed node claims.
- Uses asynchronous HTTP requests for efficient, non-blocking execution.
- Provides a visual output of the process with `rich` for enhanced user experience.
- Automatically handles error codes and exceptions during the claim process.

## Setup

### Prerequisites

- Python 3.7+ installed on your machine.
- The following Python libraries:
  - `httpx` for asynchronous HTTP requests.
  - `rich` for console output formatting.

You can install the required libraries by running:

```bash
pip install httpx rich
```

### Configuration

1. Set your **AUTH_TOKEN** and **ACCOUNT_ID** in the script. You can obtain the AUTH_TOKEN from your Epic Games account.
2. Ensure the `NODE_IDS` list contains the node IDs you wish to claim.

```python
AUTH_TOKEN = "your_auth_token_here"
ACCOUNT_ID = "your_account_id_here"
```

## Usage

To run the script, simply execute it:

```bash
python main.py
```

The script will:

1. Start claiming nodes asynchronously.
2. Output progress and results in real-time, showing the number of nodes successfully claimed and the ones that failed.
3. Provide a percentage breakdown of successful vs failed claims.

## Example Output

```bash
Claiming STW nodes... [dots spinner]
✅ Claimed: HomebaseNode:questreward_buildingresourcecap
⚠️ Node already claimed: HomebaseNode:questreward_buildingresourcecap2
❌ Failed: HomebaseNode:questreward_evolution4: Item not found

✅ 50 (75.00%)
❌ 10 (15.00%)
Finished claiming nodes!
```

## Notes

- The `NODE_IDS` list contains a large number of node IDs, which you can customize based on your needs.
- If a node has already been claimed or there's an issue with the request, it will be marked as failed, and the reason will be displayed.
- You can adjust the timeout value in the `httpx.AsyncClient` to change the duration of request retries.
