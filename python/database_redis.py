#!/usr/env python3
# coding: utf-8

import redis


def main():
    cache = redis.StrictRedis(host='localhost', port=6379)

    cache.set('blog:title', 'title_name')
    cache.set('blog:post', 'post_content')

    cache.get('blog:title')
    cache.get('blog:post')

if __name__ == '__main__':
    main()
