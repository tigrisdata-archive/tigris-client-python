PROTO_PATH=./api/proto
PROTO_FILE_PATH=${PROTO_PATH}/server/v1
GENERATED_DIR=./generated-src/

clean:
	rm -rf ${GENERATED_DIR}

generate:
	mkdir -p ${GENERATED_DIR}
	for pf in 'api.proto' 'search.proto' ; do \
		python -m grpc_tools.protoc -I ${PROTO_PATH} --python_out=${GENERATED_DIR} --grpc_python_out=${GENERATED_DIR} ${PROTO_FILE_PATH}/$${pf} ; \
	done