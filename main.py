import os
import sys
import time
import pickle
import socket
import struct
import threading
import multiprocessing
from datetime import datetime

import cv2
import logging
import numpy as np
import tensorflow as tf
from kafka import KafkaConsumer, KafkaProducer
from kafka import TopicPartition

from mface_recognition import my_face_model as recognition_face_model 
from mface_recognition.utils import load_data as load_data_face_recognition
from mface_recognition.recognition1 import recognition as face_recognition

import mysql.connector

from database.crud import Cluster, Topic, Broker, Recognite

from logger import Logger

from utils import parser


# logger
log_path = os.getcwd()
log = Logger(log_path)


def camera_recognite(source_topic, source_servers, destination_topic, destination_servers):
	try:
		# consumer from source topic
		kafka_consumer = KafkaConsumer(
			source_topic,
			group_id="default",
			value_deserializer=lambda m:pickle.loads(m),
			key_deserializer=lambda m:pickle.loads(m),
			bootstrap_servers=source_servers,
			enable_auto_commit=False) 	
		# producer to destination topic
		kafka_producer = KafkaProducer(
			value_serializer=lambda m:pickle.dumps(m),
			key_serializer=lambda m:pickle.dumps(m),
			bootstrap_servers=destination_servers)
		# model config
		recog_model = recognition_face_model.FaceModel()
		face_data = load_data_face_recognition()
		# consumer message
		for message in kafka_consumer:
			encode_face = message.value
			face = cv2.imdecode(encode_face, cv2.IMREAD_COLOR)
			face_name = face_recognition(face, recog_model, face_data)
			p = kafka_producer.send(destination_topic, value = face_name, key = message.key, timestamp_ms = message.timestamp)
			p.get()
			display_message = f"NAME: {face_name} - KEY: {message.key} - TIME: {message.timestamp}"
			print(display_message)
			log.info(display_message)
			kafka_consumer.commit()
	except Exception as e:
		# log error here
		error_message = f"{e}"
		log.error(error_message)
	finally:
		pass
	


if __name__ == "__main__":
	recognites = Recognite.get_recognites()
	for recognite in recognites:
		# source
		source_topic = Topic.get_topic(recognite.source_topic)
		source_servers = []
		source_brokers = Broker.get_brokers(source_topic.cluster_id)
		for broker in source_brokers:
			source_servers.append(broker.server)
		# destination
		destination_topic = Topic.get_topic(recognite.destination_topic)
		destination_servers = []
		destination_brokers = Broker.get_brokers(destination_topic.cluster_id)
		for broker in destination_brokers:
			destination_servers.append(broker.server)
		# print(f"source topic: {source_topic.name} - source server: {source_servers} - destination_topic: {destination_topic.name} - destination_server: {destination_servers}")
		process = multiprocessing.Process(target=camera_recognite, args=(source_topic.name, source_servers, destination_topic.name, destination_servers))
		process.start()


