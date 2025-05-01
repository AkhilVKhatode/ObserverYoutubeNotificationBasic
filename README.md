# Observer Pattern Example - YouTube Video Notification System

This project demonstrates the implementation of the **Observer Design Pattern** in Python. The system simulates a YouTube channel with different types of subscribers who are notified when a new video is uploaded.

## Project Overview

In this system:
- A **YouTube Channel** (subject) maintains a list of subscribers and notifies them whenever a new video is uploaded.
- Subscribers (observers) can be of different types, including:
  - **YouTube Subscriber** who watches the video.
  - **Email Subscriber** who receives an email notification.
  - **Push Notification Subscriber** who gets a push notification.

This example showcases the flexibility and extensibility of the Observer Pattern, where different types of subscribers can be notified in various ways when the subject state changes.

## Design Pattern: Observer

The **Observer** pattern is a behavioral design pattern where an object (subject) maintains a list of its dependents (observers) and notifies them of any changes to its state. In this example, the state change is the upload of a new video.

## Files in this Project

- **subscriber.py**: Contains the abstract `Subscriber` class and concrete subscriber classes (`YouTubeSubscriber`, `EmailSubscriber`, `PushNotificationSubscriber`).
- **youtube_channel.py**: Contains the `YouTubeChannelImpl` class, which manages subscribers and uploads videos.
- **main.py**: The main driver file that simulates the YouTube video upload and notifies subscribers.

Sample Output
After running the script, you will see the following output based on the subscribers and video uploads:
```vbnet
Alice is watching the video: Python Design Patterns Tutorial
Bob is watching the video: Python Design Patterns Tutorial
Sending email to bob@example.com: New video uploaded: Python Design Patterns Tutorial
Sending push notification to iPhone: New video uploaded: Python Design Patterns Tutorial
Alice is watching the video: Observer Pattern in Action
```

Key Concepts Demonstrated
- Observer Pattern: The core idea behind this project is the observer pattern, where an object (YouTubeChannel) notifies its subscribers when a change occurs.
- Polymorphism: Different types of subscribers implement the update method to notify them in their unique way (watching video, receiving email, etc.).
- Loose Coupling: The subscribers and the channel are loosely coupled; they interact via an abstract interface, allowing for flexibility in adding new types of subscribers.

