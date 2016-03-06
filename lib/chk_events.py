#!/usr/bin/env python3

class CheckEvents ():
    def _init_(self):
        import sqlite3 #CREATE TABLE tasks(ID INTEGER PRIMARY KEY ASC, Description TEXT, Expires INTEGER)
        self.conn = sqlite3.connect('../testdata/tasks.sqlite')
    def list_events(self):
            self.conn.execute('SELECT * FROM tasks')
        
        
