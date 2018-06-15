import os
import csv

from config import *


class Sess:
    def add(self):
        nid = str(int(self.read())+1)
        with open(nnir_path+'meta/ims.txt', 'w') as sessfile:
            sessfile.write(nid)

    def read(self):
        with open(nnir_path+'meta/ims.txt', 'r') as sessfile:
            id = sessfile.read()
            sessfile.close()
        return str(id)

    def ndir(self):
        if not os.path.exists(nnir_path+'meta/sess/'+str(self.read())):
            os.mkdir(nnir_path+'meta/sess/'+str(self.read()))


class MetaData:
    def __init__(self, writer_sess_id: int):
        self.wsess_id = str(writer_sess_id)

    def write(self, **meta):
        with open(nnir_path+'meta/sess/'+self.wsess_id+'/meta.txt', 'a') as metadata:
            for key in meta:
                for val in meta.values():
                    metadata.write(key.upper()+'='+val+'\n')

    def read(self, *tags, sess_id):
        reader = Reader(nnir_path+'meta/sess/' + str(sess_id) + '/meta.txt')
        meta = reader.clean_read()
        for mt in meta:
            for tag in tags:
                if tag.upper() == mt.split('=')[0]:
                    yield mt.split('=')[1]


class Reader:
    def __init__(self, file, delimiter='\n'):
        self.file = file
        self.format = self.file.split('.')[-1]
        self.delm = delimiter

    def read_raw(self):
        if self.format == 'csv':
            csvfile = open(self.file, 'r')
            return csv.reader(csvfile)

        elif self.format == 'txt':
            txtfile = open(self.file, 'r')
            return txtfile

    def clean_read(self):
        read = self.read_raw()
        data = []
        for row in read:
            try:
                data.append(row.split('\n')[0])
            except AttributeError:
                data.append([val for val in row])
        return data


class PathManager:
    def __init__(self):
        self.sess = Sess()
        self.sess_id = self.sess.read()
        self.Meta = MetaData(int(self.sess_id))

        raw_meta = self.Meta.read('path_file', sess_id=self.sess_id)

        meta = [mt for mt in raw_meta]

        self.pfile = meta[0]

        if not os.path.exists(nnir_path+'meta/sess/' + self.sess_id + '/impaths.csv'):
            with open(nnir_path+'meta/sess/' + self.sess_id + '/impaths.csv', 'w') as pathfile:
                pathfile.close()

    def cpaths(self):
        reader = Reader(self.pfile)
        paths = reader.clean_read()
        with open(nnir_path+'meta/sess/' + self.sess_id + '/impaths.csv', 'a') as pathfile:
            writer = csv.writer(pathfile, delimiter='\n')
            for path in paths:
                writer.writerow([path])
        return True
