# -*- coding: UTF-8 -*-
from core.Client import *


class Application(object):
    app_thread = None
    start_thread = None
    is_running = False
    client_manager = ClientManager()
    unit_case = None

    def run_case(self, case):
        if len(case.guests) <= 0:
            return

        self.unit_case = case
        for guest in case.guests:
            client = Client()
            client.ai_action = case.build_ai(client)
            client.guest_info = guest
            self.client_manager.add_client(client)

    def run_case_ex(self, case):
        if len(case.guests) <= 0:
            return

        self.unit_case = case

    def start(self):
        self.is_running = True
        self.app_thread = threading.Thread(target=self.app_proc)
        self.app_thread.setDaemon(True)
        self.app_thread.start()
        self.app_thread.join()

    def start_ex(self):
        self.is_running = True
        self.app_thread = threading.Thread(target=self.app_proc)
        self.app_thread.setDaemon(True)
        self.app_thread.start()

        self.start_thread = threading.Thread(target=self.start_proc)
        self.start_thread.setDaemon(True)
        self.start_thread.start()

    def wait(self):
        self.app_thread.join()

    def stop(self):
        self.is_running = False

    def app_proc(self):
        while self.is_running:
            self.update()
            time.sleep(0.01)

    def start_proc(self):
        cnt = 0
        for guest in self.unit_case.guests:
            client = Client()
            client.ai_action = self.unit_case.build_ai(client)
            client.guest_info = guest
            self.client_manager.add_client(client)
            cnt += 1
            if cnt < 30:
                time.sleep(10)
            else:
                time.sleep(1)


    def update(self):
        self.client_manager.update()
        self.unit_case.update()

G_App = Application()
