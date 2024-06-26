# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rService.proto\"H\n\rCreateRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0enum_partitions\x18\x02 \x01(\x05\x12\x0c\n\x04size\x18\x03 \x01(\x05\"\xaa\x01\n\x0e\x43reateResponse\x12\x33\n\npartitions\x18\x01 \x03(\x0b\x32\x1f.CreateResponse.PartitionsEntry\x12\x1b\n\x13last_partition_urls\x18\x02 \x03(\t\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x1a\x31\n\x0fPartitionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"v\n\x14SendPartitionRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0epartition_name\x18\x02 \x01(\t\x12\x16\n\x0epartition_data\x18\x03 \x01(\x0c\x12\x1b\n\x13\x63urrent_replication\x18\x04 \x01(\x05\",\n\x15SendPartitionResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\"B\n\x15ReplicationUrlRequest\x12\x16\n\x0epartition_name\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\"%\n\x16ReplicationUrlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x12\n\x10ListFilesRequest\"o\n\x11ListFilesResponse\x12,\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x1d.ListFilesResponse.FilesEntry\x1a,\n\nFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"M\n\x13SaveNodeFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0epartition_name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"\'\n\x14SaveNodeFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"2\n\x10HeartBeatRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x05\"$\n\x11HeartBeatResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x0c\x44\x61taNodeInfo\x12\x0b\n\x03url\x18\x01 \x03(\t\"$\n\x0f\x44ownloadRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"\xa0\x01\n\x10\x44ownloadResponse\x12\x35\n\npartitions\x18\x01 \x03(\x0b\x32!.DownloadResponse.PartitionsEntry\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x1a@\n\x0fPartitionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.DataNodeInfo:\x02\x38\x01\"E\n\x18\x44ownloadPartitionRequest\x12\x16\n\x0epartition_name\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\"F\n\x19\x44ownloadPartitionResponse\x12\x16\n\x0epartition_data\x18\x01 \x01(\x0c\x12\x11\n\tfile_name\x18\x02 \x01(\t\"J\n\x10ReplicateRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0epartition_name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"(\n\x11ReplicateResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\"C\n\x16\x44\x65letePartitionRequest\x12\x16\n\x0epartition_name\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\".\n\x17\x44\x65letePartitionResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\"O\n\x15\x44\x65leteNodeFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0epartition_name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\")\n\x16\x44\x65leteNodeFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9f\x03\n\x08NameNode\x12+\n\x06\x43reate\x12\x0e.CreateRequest\x1a\x0f.CreateResponse\"\x00\x12\x34\n\tListFiles\x12\x11.ListFilesRequest\x1a\x12.ListFilesResponse\"\x00\x12\x43\n\x0eReplicationUrl\x12\x16.ReplicationUrlRequest\x1a\x17.ReplicationUrlResponse\"\x00\x12=\n\x0cSaveNodeFile\x12\x14.SaveNodeFileRequest\x1a\x15.SaveNodeFileResponse\"\x00\x12\x43\n\x0e\x44\x65leteNodeFile\x12\x16.DeleteNodeFileRequest\x1a\x17.DeleteNodeFileResponse\"\x00\x12\x34\n\tHeartBeat\x12\x11.HeartBeatRequest\x1a\x12.HeartBeatResponse\"\x00\x12\x31\n\x08\x44ownload\x12\x10.DownloadRequest\x1a\x11.DownloadResponse\"\x00\x32\x98\x02\n\x08\x44\x61taNode\x12@\n\rSendPartition\x12\x15.SendPartitionRequest\x1a\x16.SendPartitionResponse\"\x00\x12L\n\x11\x44ownloadPartition\x12\x19.DownloadPartitionRequest\x1a\x1a.DownloadPartitionResponse\"\x00\x12\x34\n\tReplicate\x12\x11.ReplicateRequest\x1a\x12.ReplicateResponse\"\x00\x12\x46\n\x0f\x44\x65letePartition\x12\x17.DeletePartitionRequest\x1a\x18.DeletePartitionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATERESPONSE_PARTITIONSENTRY']._options = None
  _globals['_CREATERESPONSE_PARTITIONSENTRY']._serialized_options = b'8\001'
  _globals['_LISTFILESRESPONSE_FILESENTRY']._options = None
  _globals['_LISTFILESRESPONSE_FILESENTRY']._serialized_options = b'8\001'
  _globals['_DOWNLOADRESPONSE_PARTITIONSENTRY']._options = None
  _globals['_DOWNLOADRESPONSE_PARTITIONSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEREQUEST']._serialized_start=17
  _globals['_CREATEREQUEST']._serialized_end=89
  _globals['_CREATERESPONSE']._serialized_start=92
  _globals['_CREATERESPONSE']._serialized_end=262
  _globals['_CREATERESPONSE_PARTITIONSENTRY']._serialized_start=213
  _globals['_CREATERESPONSE_PARTITIONSENTRY']._serialized_end=262
  _globals['_SENDPARTITIONREQUEST']._serialized_start=264
  _globals['_SENDPARTITIONREQUEST']._serialized_end=382
  _globals['_SENDPARTITIONRESPONSE']._serialized_start=384
  _globals['_SENDPARTITIONRESPONSE']._serialized_end=428
  _globals['_REPLICATIONURLREQUEST']._serialized_start=430
  _globals['_REPLICATIONURLREQUEST']._serialized_end=496
  _globals['_REPLICATIONURLRESPONSE']._serialized_start=498
  _globals['_REPLICATIONURLRESPONSE']._serialized_end=535
  _globals['_LISTFILESREQUEST']._serialized_start=537
  _globals['_LISTFILESREQUEST']._serialized_end=555
  _globals['_LISTFILESRESPONSE']._serialized_start=557
  _globals['_LISTFILESRESPONSE']._serialized_end=668
  _globals['_LISTFILESRESPONSE_FILESENTRY']._serialized_start=624
  _globals['_LISTFILESRESPONSE_FILESENTRY']._serialized_end=668
  _globals['_SAVENODEFILEREQUEST']._serialized_start=670
  _globals['_SAVENODEFILEREQUEST']._serialized_end=747
  _globals['_SAVENODEFILERESPONSE']._serialized_start=749
  _globals['_SAVENODEFILERESPONSE']._serialized_end=788
  _globals['_HEARTBEATREQUEST']._serialized_start=790
  _globals['_HEARTBEATREQUEST']._serialized_end=840
  _globals['_HEARTBEATRESPONSE']._serialized_start=842
  _globals['_HEARTBEATRESPONSE']._serialized_end=878
  _globals['_DATANODEINFO']._serialized_start=880
  _globals['_DATANODEINFO']._serialized_end=907
  _globals['_DOWNLOADREQUEST']._serialized_start=909
  _globals['_DOWNLOADREQUEST']._serialized_end=945
  _globals['_DOWNLOADRESPONSE']._serialized_start=948
  _globals['_DOWNLOADRESPONSE']._serialized_end=1108
  _globals['_DOWNLOADRESPONSE_PARTITIONSENTRY']._serialized_start=1044
  _globals['_DOWNLOADRESPONSE_PARTITIONSENTRY']._serialized_end=1108
  _globals['_DOWNLOADPARTITIONREQUEST']._serialized_start=1110
  _globals['_DOWNLOADPARTITIONREQUEST']._serialized_end=1179
  _globals['_DOWNLOADPARTITIONRESPONSE']._serialized_start=1181
  _globals['_DOWNLOADPARTITIONRESPONSE']._serialized_end=1251
  _globals['_REPLICATEREQUEST']._serialized_start=1253
  _globals['_REPLICATEREQUEST']._serialized_end=1327
  _globals['_REPLICATERESPONSE']._serialized_start=1329
  _globals['_REPLICATERESPONSE']._serialized_end=1369
  _globals['_DELETEPARTITIONREQUEST']._serialized_start=1371
  _globals['_DELETEPARTITIONREQUEST']._serialized_end=1438
  _globals['_DELETEPARTITIONRESPONSE']._serialized_start=1440
  _globals['_DELETEPARTITIONRESPONSE']._serialized_end=1486
  _globals['_DELETENODEFILEREQUEST']._serialized_start=1488
  _globals['_DELETENODEFILEREQUEST']._serialized_end=1567
  _globals['_DELETENODEFILERESPONSE']._serialized_start=1569
  _globals['_DELETENODEFILERESPONSE']._serialized_end=1610
  _globals['_NAMENODE']._serialized_start=1613
  _globals['_NAMENODE']._serialized_end=2028
  _globals['_DATANODE']._serialized_start=2031
  _globals['_DATANODE']._serialized_end=2311
# @@protoc_insertion_point(module_scope)
