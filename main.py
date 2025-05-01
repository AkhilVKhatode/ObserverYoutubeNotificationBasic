from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, video: str):
        pass


class YouTubeSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, video: str):
        print(f"{self.name} is watching the video: {video}")


class EmailSubscriber(Subscriber):
    def __init__(self, email: str):
        self.email = email

    def update(self, video: str):
        print(f"Sending email to {self.email}: New video uploaded: {video}")


class PushNotificationSubscriber(Subscriber):
    def __init__(self, user_device: str):
        self.user_device = user_device

    def update(self, video: str):
        print(f"Sending push notification to {self.user_device}: New video uploaded: {video}")


class YouTubeChannel(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass


class YouTubeChannelImpl(YouTubeChannel):
    def __init__(self):
        self.subscribers = []  # List of subscribers
        self.video = ""  # The video that will be uploaded

    def add_subscriber(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.video)

    def upload_new_video(self, video: str):
        self.video = video  # Set the video that is being uploaded
        self.notify_subscribers()  # Notify all subscribers about the new video


# Main function to simulate the behavior
if __name__ == "__main__":
    # Create a YouTube channel
    channel = YouTubeChannelImpl()

    # Create subscribers
    alice = YouTubeSubscriber("Alice")
    bob = YouTubeSubscriber("Bob")

    # Subscribe to the channel
    channel.add_subscriber(alice)
    channel.add_subscriber(bob)

    # Upload a new video and notify subscribers
    channel.upload_new_video("Python Design Patterns Tutorial")
    # Output:
    # Alice is watching the video: Python Design Patterns Tutorial
    # Bob is watching the video: Python Design Patterns Tutorial

    # Remove a subscriber and upload another video
    channel.remove_subscriber(bob)
    channel.upload_new_video("Observer Pattern in Action")
    # Output:
    # Alice is watching the video: Observer Pattern in Action
