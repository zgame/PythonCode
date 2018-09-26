#! /usr/bin/env python

# See README.txt for information and build instructions.

import books_pb2 as bk


def prompt_for_address(person):
    person.id = 20
    person.name = "333"
    person.email = 'sdfsdfsdf'

    phone_number = person.phones.add()
    phone_number.number = '5555555555'
    phone_number.type = bk.Person.WORK


address_book = bk.AddressBook()
prompt_for_address(address_book.people.add())
prompt_for_address(address_book.people2)

sss = address_book.SerializeToString()
print(sss)

new_book = bk.AddressBook()
new_book.ParseFromString(sss)
print(new_book)
