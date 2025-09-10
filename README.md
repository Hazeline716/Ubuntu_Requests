# Ubuntu_Requests
Ubuntu-Inspired Image Fetcher Assignment
The Wisdom of Ubuntu: "I am because we are"

In the spirit of Ubuntu, which emphasizes community and sharing, your task is to create a program that connects to the global community of the internet, respectfully fetches shared resources, and organizes them for later appreciation.

Your Task

1.Create a Python script that:

2.Prompts the user for a URL containing an image

3.Creates a directory called "Fetched_Images" if it doesn't exist

4.Downloads the image from the provided URL

5.Saves it to the Fetched_Images directory with an appropriate filename

6.Handles errors gracefully, respecting that not all connections succeed

Requirements

1.Use the requests library to fetch the image

2.Check for HTTP errors and handle them appropriately

3.Create the directory if it doesn't exist using os.makedirs() with exist_ok=True

4.Extract the filename from the URL or generate one if not available

5.Save the image in binary mode

Ubuntu Principles to Implement

-Community: Your program should connect to the wider web community

-Respect: Handle errors gracefully without crashing

-Sharing: Organize the fetched images for later sharing

-Practicality: Create a tool that serves a real need
