Twitter Liked Tweets Downloader

This script allows you to download liked tweets from a Twitter user account using the Twitter API. It utilizes environment variables for authentication and requires the installation of the jq tool for parsing JSON responses.
Prerequisites

    Twitter Developer Account: You need to have a Twitter Developer Account to obtain the necessary API keys and tokens.
    jq Tool: Install the jq tool for parsing JSON responses. You can install it on macOS using Homebrew (brew install jq) or on Linux using your package manager (sudo apt-get install jq).
    Python 3: Ensure you have Python 3 installed on your system.

Installation

    Clone the repository to your local machine:

    bash

git clone https://github.com/yourusername/twitter-liked-tweets.git

Navigate to the project directory:

bash

cd twitter-liked-tweets

Install Python dependencies:

    pip install -r requirements.txt

Usage

    Set up environment variables:
        twitter_bearer_token: Twitter API Bearer Token.
        twitter_cookie_id: Twitter cookie ID.
        personalization_id: Personalization ID.
        twitter_user_id: Twitter user ID whose liked tweets you want to download.

    Run the script:

    python download_tweets.py

    The script will download the liked tweets of the specified Twitter user and save them to a file named tweet_ids.json.

Notes

    This script currently retrieves liked tweets in batches of 100. You can modify the script to adjust the batch size or implement pagination handling according to your needs.
    Ensure that your Twitter Developer Account has the necessary permissions to access user liked tweets.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
