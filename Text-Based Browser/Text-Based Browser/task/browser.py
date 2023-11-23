import os

import colorama as colorama
import requests
import argparse
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

my_stack = deque()
colorama.init(autoreset=True)

def create_dir(name):
    if not os.access(f"{name}", os.F_OK):
        os.mkdir(f'{name}')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help="Enter name of dir")
    args = parser.parse_args()
    if args.name:
        create_dir(args.name)
    return args.name


def find_url(url, save_dir):
    if url == 'exit':
        return True
    elif os.access(f"{save_dir}/{url}", os.F_OK):
        with open(f"{save_dir}/{url}") as f:
            print(f.read())
    elif url:
        if url.endswith(".com") or url.endswith(".org"):
            my_stack.append(url)
            new_url = 'https://' + url
            r = requests.get(new_url)
            soup = BeautifulSoup(r.content, 'html.parser')
            for i in soup.find_all("a"):
                i.string = "".join([Fore.BLUE, i.get_text(), Fore.RESET])
            text = soup.get_text()
            print(text)
            with open(f"{save_dir}/{url.rstrip('.com')}", 'w', encoding='utf-8') as f:
                f.write(text)
        else:
            print("Incorrect URL")
    elif url == 'back':
        if len(my_stack) == 0:
            return
        else:
            my_stack.pop()
            print(my_stack[0])

    else:
        print("Incorrect URL")


def main():
    name_of_dir = parse_arguments()
    while True:
        user_url = input()
        if find_url(user_url, name_of_dir):
            break


if __name__ == '__main__':
    main()
