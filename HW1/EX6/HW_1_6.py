import time
import os
import numpy as np
from PIL import Image


def read_words_list(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words


def read_words_set(filename):
    with open(filename, 'r') as file:
        words = set(file.read().split())
    return words


def compare_read_words(filename):
    list_start_time = time.time()
    words_list = read_words_list(filename)
    list_end_time = time.time()
    list_elapsed_time = list_end_time - list_start_time

    set_start_time = time.time()
    words_set = read_words_set(filename)
    set_end_time = time.time()
    set_elapsed_time = set_end_time - set_start_time

    if list_elapsed_time < set_elapsed_time:
        print("List is faster")
        print("list: ", list_elapsed_time)
        print("set: ", set_elapsed_time)
    elif list_elapsed_time > set_elapsed_time:
        print("Set is faster")
        print("list: ", list_elapsed_time)
        print("set: ", set_elapsed_time)
    else:
        print("Both are equally fast")
        print("list: ", list_elapsed_time)
        print("set: ", set_elapsed_time)

    return


def find_states_same_row(filename):
    with open(filename, 'r') as file:
        states = file.read().split()

    rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    same_row_states = []

    for state in states:
        row_found = False
        for row in rows:
            if all(char.lower() in row for char in state):
                same_row_states.append(state)
                row_found = True
                break
        if not row_found:
            continue

    return same_row_states


def calc(op, a, b):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    ops = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    if op not in ops:
        return None
    return ops[op](a, b)


def apply(func, iterable):
    for val in iterable:
        yield func(val)


def my_filter(func, iterable):
    filtered_list = []
    for val in iterable:
        if func(val):
            filtered_list.append(val)
    return filtered_list


def get_positive_numbers():
    numbers = input("Enter comma-separated numbers: ").split(',')
    return [n for n in numbers if int(n) > 0]


def timer(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time elapsed: {duration:.2f} seconds")
    return result


import math


def sqrt_numbers(strings):
    return [math.sqrt(float(s)) if s.isnumeric() else "" for s in strings]


def dice():
    return [(die1, die2, die3) for die1 in range(1, 7) for die2 in range(1, 7) for die3 in range(1, 7)]


def len_of_words(words):
    return [len(w) for w in words]


def get_alphabet():
    return ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)]) + ''.join(
        [chr(i) for i in range(ord('A'), ord('Z') + 1)])


def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def generate_full_names(first_name, last_name, minimum=None):
    full_names = []
    for f in first_name.split():
        for l in last_name.split():
            full_name = f + ' ' + l
            if minimum is None or len(full_name) >= minimum:
                full_names.append(full_name)
    return full_names


def find_black_pixels(image_path, threshold=50):
    image = np.array(Image.open(image_path))
    black_pixels = []
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            pixel = image[y][x]
            if np.all(pixel <= threshold):
                black_pixels.append(y)
                break
    print(black_pixels)
    sentence = ''.join(chr(i) for i in black_pixels)
    return sentence


def group_by(func, arg_list):
    result_dict = {}
    for arg in arg_list:
        result = func(arg)
        if result in result_dict:
            result_dict[result].append(arg)
        else:
            result_dict[result] = [arg]
    return result_dict


def zip_with(func, *iterables):
    result = []
    for args in zip(*iterables):
        result.append(func(*args))
    return tuple(result)


def encrypt_sentence(sentence):
    mx_let = max(ord(c) for c in sentence) + 1
    image = Image.new('RGB', (mx_let, mx_let), color=(255, 255, 255))
    pixels = image.load()

    for i, char in enumerate(sentence):
        pixel_value = ord(char)
        col_index = i
        row_index = pixel_value
        pixels[col_index, row_index] = (0, 0, 0)

    # Save the image in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "encrypted_image.png")
    image.save(image_path)

    return image


