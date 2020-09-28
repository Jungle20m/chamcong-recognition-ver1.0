from sqlalchemy.orm import Session
from . import models, schemas

from .database import chamcong_session
from .database import base_session



class Cluster:
    @staticmethod
    def get_cluster():
        try:
            db = base_session()
            return db.query(models.Cluster).all()
        finally:
            db.close()
            

class Broker:
    @staticmethod
    def get_brokers(cluster_id: int):
        try:
            db = base_session()
            return db.query(models.Broker).filter(models.Broker.cluster_id==cluster_id).all()
        finally:
            db.close()


class Topic:
    @staticmethod
    def get_topic(id: int):
        try:
            db = base_session()
            return db.query(models.Topic).filter(models.Topic.id==id).first()
        finally:
            db.close()


class Recognite():
    @staticmethod
    def get_recognites():
        try:
            db = chamcong_session()
            return db.query(models.Recognite).all()
        finally:
            db.close()