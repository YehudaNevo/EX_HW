import os
import datetime
import random
import re



def get_files_in_directory(path):
    file_names = []
    with os.scandir(path) as directory:
        for entry in directory:
            if entry.is_file() and entry.name.startswith("deep"):
                file_names.append(os.path.basename(entry.path))
    return file_names


def random_date_between_dates(start_date, end_date):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    delta = end - start
    return (start + datetime.timedelta(days=random.randint(0, delta.days))).strftime("%A, %B %d, %Y")


def join(*args, sep='-'):
    result = []
    for i, lst in enumerate(args):
        result.extend(lst)
        if i < len(args) - 1 and sep:
            result.append(sep)
    return result


def get_recipe_price(prices, optionals=None, **ingredients):
    total_price = 0
    for ingredient, amount in ingredients.items():
        if ingredient not in prices:
            raise ValueError(f"{ingredient} is not a valid ingredient.")
        if optionals and ingredient in optionals:
            continue
        price_per_100g = prices[ingredient]
        ingredient_price = (price_per_100g / 100) * amount
        total_price += ingredient_price
    return round(total_price, 2)


def perfect_numbers():
    """Generate all perfect numbers."""
    n = 1
    while True:
        divisors = [i for i in range(1, n) if n % i == 0]
        if sum(divisors) == n:
            yield n
        n += 1


def extract_messages(filename):  # TODO  fix it.
    """Extract hidden messages from a binary file."""
    msg_buffer = ''
    with open('resources/logo.jpg', 'rb') as f:
        while True:
            chunk = f.read(1024)  # Read 1 KB at a time
            if not chunk:  # End of file
                break
            for char in chunk:
                if char in range(97, 123):  # Check if char is lowercase
                    msg_buffer += chr(char)
                    if msg_buffer[-1] == '!':  # Found a complete message
                        yield msg_buffer[:-1]  # Yield the message without the '!'
                        msg_buffer = ''
                else:
                    msg_buffer = ''  # Reset buffer if non-message char is found


def combine_iterables(*iterables):
    """Combine two or more iterables into tuples."""
    iters = [iter(it) for it in iterables]
    while True:
        try:
            items = tuple(next(it) for it in iters)
            yield items
        except StopIteration:
            return


def modify_chapter_name_and_copy_files(folder_path, new_folder_path):
    # Create the new directory if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                contents = file.read()
                chapter_number = filename.split('.')[0]
                chapter_title = re.search(
                    fr'<option value="{chapter_number}">(Chapter {chapter_number}:[^<]+)</option>',
                    contents)

                if chapter_title:
                    chapter_title = chapter_title.group(1)
                else:
                    chapter_title = "Chapter not found"
                chapter_name = re.search(r'id="chapter-title">Chapter (\d+): ([^<]+)<', contents).group(2)

                if chapter_name:
                    new_chapter_name = f"{filename.split('.')[0]}: {chapter_title}"
                    new_contents = re.sub(r'id="chapter-title">Chapter (\d+): ([^<]+)<',
                                          f'id="chapter-title">{new_chapter_name}<', contents)
                    # Replace the old chapter name with the new chapter name

                    new_filename = f"{filename.split('.')[0]}.html"
                    new_file_path = os.path.join(new_folder_path, new_filename)
                    with open(new_file_path, 'w') as new_file:
                        new_file.write(new_contents)  # Write the modified contents to the new file
                    print(f"{filename} ->  new chapter is :  {new_chapter_name}")
                else:
                    print(f"{filename}: Chapter name not found")


