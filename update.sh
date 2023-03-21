# This is a script to build a new image and push it to the registry. It also takes an argument for the new tag

# Check if the user has provided a tag
if [ -z "$1" ]; then
    echo "No tag provided"
    exit 1
fi

# Build the image
docker build -t  ghcr.io/jthesaw/gpt3-signalbot:$1 .

# Push the image to the registry
docker push ghcr.io/jthesaw/gpt3-signalbot:$1

# Stop and remove the old container
docker stop gpt3-bot
docker rm gpt3-bot

# Run the image
docker run -d --network="host" --env-file .env --name gpt3-bot ghcr.io/jthesaw/gpt3-signalbot:$1

