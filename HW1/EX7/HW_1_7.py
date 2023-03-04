import math


class Poll:
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.votes = [0] * len(options)

    def vote(self, option_index):
        if 0 <= option_index < len(self.options):
            self.votes[option_index] += 1
        else:
            raise ValueError("Invalid option index")

    def add_option(self, option):
        self.options.append(option)
        self.votes.append(0)

    def remove_option(self, option_index):
        if 0 <= option_index < len(self.options):
            self.options.pop(option_index)
            self.votes.pop(option_index)
        else:
            raise ValueError("Invalid option index")

    def get_votes(self):
        return self.votes

    def get_winner(self):
        max_votes = max(self.votes)
        if self.votes.count(max_votes) == 1:
            return self.options[self.votes.index(max_votes)]
        else:
            return "Tie"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx ** 2 + dy ** 2)


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False  # Added to track whether message has been read
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_msgs=None):
        """Read a number of messages in a user's inbox.

        :param str username: The name of the user whose inbox we want to read.
        :param int num_msgs: Optional, the number of messages to read. Default is None, which will read all messages.
        :return: A list of dictionaries representing the messages read.
        :rtype: list[dict]
        """
        user_box = self.boxes[username]
        if num_msgs is None:
            num_msgs = len(user_box)
        msgs = []
        for msg in user_box:
            if not msg['read']:
                msgs.append(msg)
                msg['read'] = True
            if len(msgs) == num_msgs:
                break
        return msgs

    def search_inbox(self, username, search_string):
        """Search for messages in a user's inbox containing a search string.

        :param str username: The name of the user whose inbox we want to search.
        :param str search_string: The string to search for.
        :return: A list of dictionaries representing the messages containing the search string.
        :rtype: list[dict]
        """
        user_box = self.boxes[username]
        found_msgs = []
        for msg in user_box:
            if search_string in msg['body']:
                found_msgs.append(msg)
        return found_msgs


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.exp = 0
        self.level = 1
        self.nemeses = []
        self.attacked_by = []

    def attack(self, enemy_name=None):
        if enemy_name is None:
            enemy = self.nemeses[-1]
        else:
            for enemy in self.nemeses:
                if enemy.name == enemy_name:
                    break
            else:
                raise ValueError(f"No enemy with name {enemy_name} found")

        damage = random.randint(5, 20) * self.level
        enemy.take_damage(damage)

    def revive(self):
        self.hp = 100
        if self.hp <= 0:
            self.hp = 1
            self.attacked_by.append("Unknown")


class Enemy:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} has been defeated!")


class PostOffice2:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, recipient, num_msgs=None):
        """Read messages in a recipient's inbox.

        :param str recipient: The message recipient's username.
        :param int num_msgs: The number of messages to read.
        :return: A list of messages.
        :rtype: list
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        if num_msgs is None:
            num_msgs = len(user_box)
        messages = []
        for i in range(num_msgs):
            if not user_box:
                break
            msg = user_box.pop(0)
            msg['read'] = True
            messages.append(msg)
        return messages

    def search_inbox(self, recipient, search_string):
        """Search a recipient's inbox for messages containing a string.

        :param str recipient: The message recipient's username.
        :param str search_string: The string to search for.
        :return: A list of matching messages.
        :rtype: list
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        matches = []
        for msg in user_box:
            if search_string in msg['body']:
                matches.append(msg)
        return matches

    def __str__(self):
        """String representation of the PostOffice.

        :return: A string representation of the PostOffice.
        :rtype: str
        """
        out = ''
        for user, inbox in self.boxes.items():
            out += f'{user}:\n'
            if not inbox:
                out += 'No messages.\n'
            for msg in inbox:
                out += f'Message {msg["id"]} from {msg["sender"]}: {msg["body"]}\n'
        return out


import random


class Player2:
    """
    A class representing a player in a game.

    Attributes:
        name (str): The name of the player.
        hp (int): The player's health points, initialized to 100.
        exp (int): The player's experience points, initialized to 0.
        level (int): The player's level, initialized to 1.
        nemeses (list): A list of the player's enemies.

    Methods:
        attack(enemy_name=None):
            Attacks the specified enemy or the last enemy in the list if no name is provided.
            Returns True if the attack is successful, False otherwise.
        revive():
            Restores the player's health points to their initial value.
    """

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.exp = 0
        self.level = 1
        self.nemeses = []

    def attack(self, enemy_name=None):
        """
        Attacks the specified enemy or the last enemy in the list if no name is provided.
        Returns True if the attack is successful, False otherwise.
        """
        if not self.nemeses:
            return False

        if enemy_name:
            for enemy in self.nemeses:
                if enemy['name'] == enemy_name:
                    damage = random.randint(5, 20) * self.level
                    enemy['hp'] -= damage
                    if enemy['hp'] <= 0:
                        self.nemeses.remove(enemy)
                    self.exp += damage
                    return True
        else:
            enemy = self.nemeses[-1]
            damage = random.randint(5, 20) * self.level
            enemy['hp'] -= damage
            if enemy['hp'] <= 0:
                self.nemeses.remove(enemy)
            self.exp += damage
            return True

        return False

    def revive(self):
        """
        Restores the player's health points to their initial value.
        """
        self.hp = 100


class Square:
    def __init__(self, size):
        self.size = size

    def get_surface(self):
        return self.size ** 2

    def get_perimeter(self):
        return 4 * self.size


class Cube:
    def __init__(self, size, color):
        self.base = Square(size)
        self.color = color
        self.volume = self.base.get_surface() * size

    def get_volume(self):
        return self.volume


class CubeTower:
    def __init__(self):
        self.cubes = []

    def can_place_cube(self, cube):
        if not self.cubes:
            return True
        else:
            top_cube = self.cubes[-1]
            return (top_cube.base.size > cube.base.size) and (top_cube.color != cube.color)

    def add_cube(self, cube):
        if self.can_place_cube(cube):
            self.cubes.append(cube)
            return True
        else:
            return False

    def __str__(self):
        res = ""
        for i, cube in enumerate(self.cubes):
            res += f"{i+1}-Cube: base-{cube.base.size}x{cube.base.size} color:{cube.color}\n"
        return res
