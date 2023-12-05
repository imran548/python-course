import datetime


def publish_blog_post(title, author, content):
    '''

    :param title:
    :param author:
    :param content:
    :return:
    '''
    # Generate a timestamp for the current date
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the formatted blog post
    formatted_post = f"Title: {title}\nAuthor: {author}\nDate: {timestamp}\n\n{content}"

    # Save the blog post to a file or publish it to a blogging platform
    # Replace this with your actual publishing logic

    print("Blog post published successfully!")


# Example usage
author = "John Doe"
content = "This is a sample blog post content."
title = "Python Automation"

publish_blog_post(title, author, content)
