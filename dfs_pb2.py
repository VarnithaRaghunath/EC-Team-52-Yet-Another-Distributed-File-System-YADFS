# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dfs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdfs.proto\x12\x03\x64\x66s\"\x15\n\x05testM\x12\x0c\n\x04word\x18\x01 \x01(\t\"H\n\rDataNodeStats\x12\x11\n\tcpu_usage\x18\x01 \x01(\t\x12\x12\n\ndisk_space\x18\x02 \x01(\t\x12\x10\n\x08used_mem\x18\x03 \x01(\t\"\x07\n\x05\x45mpty\"\x1c\n\x08UserInfo\x12\x10\n\x08username\x18\x01 \x01(\t\"2\n\x0cUserFileList\x12\x11\n\tfilenames\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\".\n\x08\x46ileInfo\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"\'\n\x03\x41\x63k\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"<\n\x08\x46ileData\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"Q\n\rFileDataChunk\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x0e\n\x06seq_no\x18\x04 \x01(\x05\"G\n\x11\x46ileDataChunkInfo\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0e\n\x06seq_no\x18\x03 \x01(\x05\x32\xba\x04\n\x13\x44\x61taTransferService\x12!\n\x07Message\x12\n.dfs.testM\x1a\n.dfs.testM\x12\'\n\nUploadFile\x12\r.dfs.FileData\x1a\x08.dfs.Ack(\x01\x12.\n\x0c\x44ownloadFile\x12\r.dfs.FileInfo\x1a\r.dfs.FileData0\x01\x12%\n\nFileSearch\x12\r.dfs.FileInfo\x1a\x08.dfs.Ack\x12*\n\rReplicateFile\x12\r.dfs.FileData\x1a\x08.dfs.Ack(\x01\x12,\n\x08\x46ileList\x12\r.dfs.UserInfo\x1a\x11.dfs.UserFileList\x12%\n\nFileDelete\x12\r.dfs.FileInfo\x1a\x08.dfs.Ack\x12\'\n\nUpdateFile\x12\r.dfs.FileData\x1a\x08.dfs.Ack(\x01\x12\x30\n\x0eStoreFileChunk\x12\x12.dfs.FileDataChunk\x1a\x08.dfs.Ack(\x01\x12<\n\x0cGetFileChunk\x12\x16.dfs.FileDataChunkInfo\x1a\x12.dfs.FileDataChunk0\x01\x12\x31\n\x0fIsDataNodeAlive\x12\n.dfs.Empty\x1a\x12.dfs.DataNodeStats\x12\x33\n\x0f\x44\x65leteFileChunk\x12\x16.dfs.FileDataChunkInfo\x1a\x08.dfs.AckB\x02H\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dfs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001'
  _globals['_TESTM']._serialized_start=18
  _globals['_TESTM']._serialized_end=39
  _globals['_DATANODESTATS']._serialized_start=41
  _globals['_DATANODESTATS']._serialized_end=113
  _globals['_EMPTY']._serialized_start=115
  _globals['_EMPTY']._serialized_end=122
  _globals['_USERINFO']._serialized_start=124
  _globals['_USERINFO']._serialized_end=152
  _globals['_USERFILELIST']._serialized_start=154
  _globals['_USERFILELIST']._serialized_end=204
  _globals['_FILEINFO']._serialized_start=206
  _globals['_FILEINFO']._serialized_end=252
  _globals['_ACK']._serialized_start=254
  _globals['_ACK']._serialized_end=293
  _globals['_FILEDATA']._serialized_start=295
  _globals['_FILEDATA']._serialized_end=355
  _globals['_FILEDATACHUNK']._serialized_start=357
  _globals['_FILEDATACHUNK']._serialized_end=438
  _globals['_FILEDATACHUNKINFO']._serialized_start=440
  _globals['_FILEDATACHUNKINFO']._serialized_end=511
  _globals['_DATATRANSFERSERVICE']._serialized_start=514
  _globals['_DATATRANSFERSERVICE']._serialized_end=1084
# @@protoc_insertion_point(module_scope)
