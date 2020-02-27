#!/usr/bin/env python3

import argparse, jinja2, sys, yaml, pprint

def jinjaEnv(directory):
    env = jinja2.Environment(
        block_start_string='(@',
        block_end_string='@)',
        variable_start_string='(*',
        variable_end_string='*)',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(directory),
    )
    return env

def buildFormatTemplate(templateRoot, template, context, output):
    print(jinjaEnv(templateRoot).get_template(template).render(context), file=output)

def main():
    parser = argparse.ArgumentParser(
        description="Prepare and compile a DeGeŠ seminar competition from repository",
    )
    parser.add_argument('template',     type=argparse.FileType('r')) 
    parser.add_argument('context',      type=argparse.FileType('r'))
    parser.add_argument('output',       nargs='?', default=sys.stdout, type=argparse.FileType('w'))
    parser.add_argument('-b', '--boha',  action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')

    args = parser.parse_args()

    buildFormatTemplate('.', args.template.name, yaml.load(args.context), args.output)

main()
