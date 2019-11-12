# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


import argparse
import datetime
import io
import os
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description='find old pages in dokuwiki')
    parser.add_argument('meta_directory', help='Path name of meta-directory. Example: /srv/www/vhosts/example.com/dokuwiki/data/meta')
    parser.add_argument('user_name', help='Find old pages of this user.')
    parser.add_argument('--min_age', default=36, help='Unit months. 12 means the articles should be unchanged since one year.', type=int)
    parser.add_argument('--percent',
                        help='90 means most of the changes are from the given user.', type=int, default=40)
    parser.add_argument('--output_template', default='https://example.com/index.html/doku.php?id={}')
    args = parser.parse_args()
    min_age = datetime.timedelta(days=(365.0/12.0)*args.min_age)
    percent_edits = args.percent/100.0
    dates = defaultdict(list)
    for file in sorted(os.listdir(args.meta_directory)):
        if not file.endswith('.changes'):
            continue
        file = os.path.join(args.meta_directory, file)
        for user, dt, file in handle_file(file, args.user_name, min_age, percent_edits):
            url = args.output_template.format(os.path.basename(file)[:-len('.changes')])
            dates[dt].append('{user} {dt} {url}'.format(user=user, dt=dt, url=url))
    for dt, lines in sorted(dates.items()):
        for line in lines:
            print(line)


def handle_file(file, user, min_age, percent_edits):
    seen_users = []
    state = None
    for line in io.open(file, encoding='utf8'):
        line = line.split('\t')
        dt = datetime.datetime.fromtimestamp(int(line[0]))
        seen_users.append(line[4])
        state = line[2]
    if not seen_users:
        return
    if state in ['D']:
        return
    if dt + min_age > datetime.datetime.now():
        return
    count = seen_users.count(user)
    if not count:
        return
    if (len(seen_users) / float(count)) > percent_edits:
        yield (user, dt, file)

if __name__ == '__main__':
    main()