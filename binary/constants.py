BYTE_SIZE_IN_BYTES = 1
BOOLEAN_SIZE_IN_BYTES = 1
SHORT_SIZE_IN_BYTES = 2
INT_SIZE_IN_BYTES = 4
LONG_SIZE_IN_BYTES = 8
UUID_SIZE_IN_BYTES = 17

FRAME_LENGTH_OFFSET = 0
FLAGS_OFFSET = FRAME_LENGTH_OFFSET + INT_SIZE_IN_BYTES
SIZE_OF_FRAME_LENGTH_AND_FLAGS = FLAGS_OFFSET + SHORT_SIZE_IN_BYTES

TYPE_FIELD_OFFSET = 0
CORRELATION_ID_FIELD_OFFSET = TYPE_FIELD_OFFSET + INT_SIZE_IN_BYTES
PARTITION_ID_FIELD_OFFSET = CORRELATION_ID_FIELD_OFFSET + LONG_SIZE_IN_BYTES
REQUEST_FIX_SIZED_PARAMS_OFFSET = PARTITION_ID_FIELD_OFFSET + INT_SIZE_IN_BYTES
RESPONSE_FIX_SIZED_PARAMS_OFFSET = CORRELATION_ID_FIELD_OFFSET + LONG_SIZE_IN_BYTES
EVENT_FIX_SIZED_PARAMS_OFFSET = PARTITION_ID_FIELD_OFFSET + INT_SIZE_IN_BYTES

DEFAULT_FLAGS = 0
BEGIN_FRAGMENT_FLAG = 1 << 15
END_FRAGMENT_FLAG = 1 << 14
UNFRAGMENTED_MESSAGE = BEGIN_FRAGMENT_FLAG | END_FRAGMENT_FLAG
IS_FINAL_FLAG = 1 << 13
BEGIN_DATA_STRUCTURE_FLAG = 1 << 12
END_DATA_STRUCTURE_FLAG = 1 << 11
IS_NULL_FLAG = 1 << 10
IS_EVENT_FLAG = 1 << 9
