#! /usr/bin/env python

# See README.txt for information and build instructions.

import websockets_protocol.procotol.books_pb2 as bk
import time
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

def PromptForAddress(person):
  person.id = 20
  person.name = "333"
  person.email = 'sdfsdfsdf'

  phone_number = person.phones.add()
  phone_number.number = '5555555555'
  phone_number.type = bk.Person.WORK



address_book = bk.AddressBook()
PromptForAddress(address_book.people.add())



sss = address_book.SerializeToString()
print(sss)

newbook = bk.AddressBook()
newbook.ParseFromString(sss)
print(newbook)

