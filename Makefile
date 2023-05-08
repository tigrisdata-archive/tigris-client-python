BASE=$(realpath .)
PROTO_BASE=${BASE}/api/proto
TIGRIS_PROTO_SRC=${PROTO_BASE}/server/v1
DEPS_PROTO_DIR="${PROTO_BASE}/google/api ${PROTO_BASE}/openapiv3"
GENERATED_DIR=${BASE}/api/generated

define fix_import
	rp="..." && \
	if [[ ${1} =~ "openapi" ]] ; then \
		rp=".." ; \
	fi && \
	sed -i '' "s/from google.api/from $${rp}google.api/g" ${1} && \
	sed -i '' "s/from openapiv3/from $${rp}openapiv3/g" ${1} && \
	sed -i '' "s/from server.v1/from $${rp}server.v1/g" ${1}
endef

clean:
	rm -rf ${GENERATED_DIR}

generate: generate_api fix_imports

generate_api:
	mkdir -p ${GENERATED_DIR} && \
	cd ${GENERATED_DIR} && \
	for dp_dir in "${DEPS_PROTO_DIR}" ; do \
	  for pf in $$(find $${dp_dir} -type f -name "*.proto") ; do \
		python -m grpc_tools.protoc --proto_path=${PROTO_BASE} \
  			--python_out=. --pyi_out=. --grpc_python_out=. $${pf} ; \
	  done \
	done && \
	for pf in "api.proto" "search.proto" ; do \
	  python -m grpc_tools.protoc --proto_path=${PROTO_BASE} \
	  	  --python_out=. --pyi_out=. --grpc_python_out=. ${TIGRIS_PROTO_SRC}/$${pf} ; \
  	done

fix_imports:
	echo "renaming imports in generated api files" && \
	for f in $$(find ${GENERATED_DIR} -type f -name "*pb2*py*") ; do \
	  	$(call fix_import,$${f}) ; \
	done