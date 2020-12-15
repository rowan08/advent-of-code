import re


with open('input.txt') as f:
    data = list(map(str.strip, f))


def is_valid_by_count(password_string):
    password_regex = re.compile(
        r'(?P<minimum>\d+)-(?P<maximum>\d+) (?P<character>\w): '
        r'(?P<password>\w+)'
    )
    variables = password_regex.match(password_string).groupdict()

    character, password, minimum, maximum = (
        variables['character'],
        variables['password'],
        int(variables['minimum']),
        int(variables['maximum']) + 1,
    )

    return password.count(character) in range(minimum, maximum)


def is_valid_by_position(password_string):
    password_regex = re.compile(
        r'(?P<include_post>\d+)-(?P<exclude_post>\d+) (?P<character>\w): '
        r'(?P<password>\w+)'
    )
    variables = password_regex.match(password_string).groupdict()

    character, password, include_post, exclude_post = (
        variables['character'],
        variables['password'],
        int(variables['include_post']) - 1,
        int(variables['exclude_post']) - 1,
    )

    return (
        (password[include_post] == character)
        + (password[exclude_post] == character)
    ) == 1


total_valid_by_count = 0
total_valid_by_postition = 0

for password in data:
    if is_valid_by_count(password):
        total_valid_by_count += 1

    if is_valid_by_position(password):
        total_valid_by_postition += 1

print(
    f'Total valid:\n By count: {total_valid_by_count}'
    f'\n By position: {total_valid_by_postition}'
)
