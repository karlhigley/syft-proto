// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: syft_proto/types/torch/v1/device.proto

package org.openmined.syftproto.types.torch.v1;

public final class DeviceOuterClass {
  private DeviceOuterClass() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  public interface DeviceOrBuilder extends
      // @@protoc_insertion_point(interface_extends:syft_proto.types.torch.v1.Device)
      com.google.protobuf.MessageOrBuilder {

    /**
     * <code>string type = 1[json_name = "type"];</code>
     * @return The type.
     */
    java.lang.String getType();
    /**
     * <code>string type = 1[json_name = "type"];</code>
     * @return The bytes for type.
     */
    com.google.protobuf.ByteString
        getTypeBytes();
  }
  /**
   * Protobuf type {@code syft_proto.types.torch.v1.Device}
   */
  public  static final class Device extends
      com.google.protobuf.GeneratedMessageV3 implements
      // @@protoc_insertion_point(message_implements:syft_proto.types.torch.v1.Device)
      DeviceOrBuilder {
  private static final long serialVersionUID = 0L;
    // Use Device.newBuilder() to construct.
    private Device(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
      super(builder);
    }
    private Device() {
      type_ = "";
    }

    @java.lang.Override
    @SuppressWarnings({"unused"})
    protected java.lang.Object newInstance(
        UnusedPrivateParameter unused) {
      return new Device();
    }

    @java.lang.Override
    public final com.google.protobuf.UnknownFieldSet
    getUnknownFields() {
      return this.unknownFields;
    }
    private Device(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      this();
      if (extensionRegistry == null) {
        throw new java.lang.NullPointerException();
      }
      com.google.protobuf.UnknownFieldSet.Builder unknownFields =
          com.google.protobuf.UnknownFieldSet.newBuilder();
      try {
        boolean done = false;
        while (!done) {
          int tag = input.readTag();
          switch (tag) {
            case 0:
              done = true;
              break;
            case 10: {
              java.lang.String s = input.readStringRequireUtf8();

              type_ = s;
              break;
            }
            default: {
              if (!parseUnknownField(
                  input, unknownFields, extensionRegistry, tag)) {
                done = true;
              }
              break;
            }
          }
        }
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        throw e.setUnfinishedMessage(this);
      } catch (java.io.IOException e) {
        throw new com.google.protobuf.InvalidProtocolBufferException(
            e).setUnfinishedMessage(this);
      } finally {
        this.unknownFields = unknownFields.build();
        makeExtensionsImmutable();
      }
    }
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return org.openmined.syftproto.types.torch.v1.DeviceOuterClass.internal_static_syft_proto_types_torch_v1_Device_descriptor;
    }

    @java.lang.Override
    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return org.openmined.syftproto.types.torch.v1.DeviceOuterClass.internal_static_syft_proto_types_torch_v1_Device_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.class, org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.Builder.class);
    }

    public static final int TYPE_FIELD_NUMBER = 1;
    private volatile java.lang.Object type_;
    /**
     * <code>string type = 1[json_name = "type"];</code>
     * @return The type.
     */
    public java.lang.String getType() {
      java.lang.Object ref = type_;
      if (ref instanceof java.lang.String) {
        return (java.lang.String) ref;
      } else {
        com.google.protobuf.ByteString bs = 
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        type_ = s;
        return s;
      }
    }
    /**
     * <code>string type = 1[json_name = "type"];</code>
     * @return The bytes for type.
     */
    public com.google.protobuf.ByteString
        getTypeBytes() {
      java.lang.Object ref = type_;
      if (ref instanceof java.lang.String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        type_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }

    private byte memoizedIsInitialized = -1;
    @java.lang.Override
    public final boolean isInitialized() {
      byte isInitialized = memoizedIsInitialized;
      if (isInitialized == 1) return true;
      if (isInitialized == 0) return false;

      memoizedIsInitialized = 1;
      return true;
    }

    @java.lang.Override
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      if (!getTypeBytes().isEmpty()) {
        com.google.protobuf.GeneratedMessageV3.writeString(output, 1, type_);
      }
      unknownFields.writeTo(output);
    }

    @java.lang.Override
    public int getSerializedSize() {
      int size = memoizedSize;
      if (size != -1) return size;

      size = 0;
      if (!getTypeBytes().isEmpty()) {
        size += com.google.protobuf.GeneratedMessageV3.computeStringSize(1, type_);
      }
      size += unknownFields.getSerializedSize();
      memoizedSize = size;
      return size;
    }

    @java.lang.Override
    public boolean equals(final java.lang.Object obj) {
      if (obj == this) {
       return true;
      }
      if (!(obj instanceof org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device)) {
        return super.equals(obj);
      }
      org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device other = (org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device) obj;

      if (!getType()
          .equals(other.getType())) return false;
      if (!unknownFields.equals(other.unknownFields)) return false;
      return true;
    }

    @java.lang.Override
    public int hashCode() {
      if (memoizedHashCode != 0) {
        return memoizedHashCode;
      }
      int hash = 41;
      hash = (19 * hash) + getDescriptor().hashCode();
      hash = (37 * hash) + TYPE_FIELD_NUMBER;
      hash = (53 * hash) + getType().hashCode();
      hash = (29 * hash) + unknownFields.hashCode();
      memoizedHashCode = hash;
      return hash;
    }

    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        java.nio.ByteBuffer data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        java.nio.ByteBuffer data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessageV3
          .parseWithIOException(PARSER, input);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessageV3
          .parseWithIOException(PARSER, input, extensionRegistry);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessageV3
          .parseDelimitedWithIOException(PARSER, input);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessageV3
          .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessageV3
          .parseWithIOException(PARSER, input);
    }
    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessageV3
          .parseWithIOException(PARSER, input, extensionRegistry);
    }

    @java.lang.Override
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder() {
      return DEFAULT_INSTANCE.toBuilder();
    }
    public static Builder newBuilder(org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device prototype) {
      return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
    }
    @java.lang.Override
    public Builder toBuilder() {
      return this == DEFAULT_INSTANCE
          ? new Builder() : new Builder().mergeFrom(this);
    }

    @java.lang.Override
    protected Builder newBuilderForType(
        com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
      Builder builder = new Builder(parent);
      return builder;
    }
    /**
     * Protobuf type {@code syft_proto.types.torch.v1.Device}
     */
    public static final class Builder extends
        com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
        // @@protoc_insertion_point(builder_implements:syft_proto.types.torch.v1.Device)
        org.openmined.syftproto.types.torch.v1.DeviceOuterClass.DeviceOrBuilder {
      public static final com.google.protobuf.Descriptors.Descriptor
          getDescriptor() {
        return org.openmined.syftproto.types.torch.v1.DeviceOuterClass.internal_static_syft_proto_types_torch_v1_Device_descriptor;
      }

      @java.lang.Override
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
          internalGetFieldAccessorTable() {
        return org.openmined.syftproto.types.torch.v1.DeviceOuterClass.internal_static_syft_proto_types_torch_v1_Device_fieldAccessorTable
            .ensureFieldAccessorsInitialized(
                org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.class, org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.Builder.class);
      }

      // Construct using org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.newBuilder()
      private Builder() {
        maybeForceBuilderInitialization();
      }

      private Builder(
          com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
        super(parent);
        maybeForceBuilderInitialization();
      }
      private void maybeForceBuilderInitialization() {
        if (com.google.protobuf.GeneratedMessageV3
                .alwaysUseFieldBuilders) {
        }
      }
      @java.lang.Override
      public Builder clear() {
        super.clear();
        type_ = "";

        return this;
      }

      @java.lang.Override
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return org.openmined.syftproto.types.torch.v1.DeviceOuterClass.internal_static_syft_proto_types_torch_v1_Device_descriptor;
      }

      @java.lang.Override
      public org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device getDefaultInstanceForType() {
        return org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.getDefaultInstance();
      }

      @java.lang.Override
      public org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device build() {
        org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return result;
      }

      @java.lang.Override
      public org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device buildPartial() {
        org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device result = new org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device(this);
        result.type_ = type_;
        onBuilt();
        return result;
      }

      @java.lang.Override
      public Builder clone() {
        return super.clone();
      }
      @java.lang.Override
      public Builder setField(
          com.google.protobuf.Descriptors.FieldDescriptor field,
          java.lang.Object value) {
        return super.setField(field, value);
      }
      @java.lang.Override
      public Builder clearField(
          com.google.protobuf.Descriptors.FieldDescriptor field) {
        return super.clearField(field);
      }
      @java.lang.Override
      public Builder clearOneof(
          com.google.protobuf.Descriptors.OneofDescriptor oneof) {
        return super.clearOneof(oneof);
      }
      @java.lang.Override
      public Builder setRepeatedField(
          com.google.protobuf.Descriptors.FieldDescriptor field,
          int index, java.lang.Object value) {
        return super.setRepeatedField(field, index, value);
      }
      @java.lang.Override
      public Builder addRepeatedField(
          com.google.protobuf.Descriptors.FieldDescriptor field,
          java.lang.Object value) {
        return super.addRepeatedField(field, value);
      }
      @java.lang.Override
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device) {
          return mergeFrom((org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }

      public Builder mergeFrom(org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device other) {
        if (other == org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device.getDefaultInstance()) return this;
        if (!other.getType().isEmpty()) {
          type_ = other.type_;
          onChanged();
        }
        this.mergeUnknownFields(other.unknownFields);
        onChanged();
        return this;
      }

      @java.lang.Override
      public final boolean isInitialized() {
        return true;
      }

      @java.lang.Override
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device parsedMessage = null;
        try {
          parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
        } catch (com.google.protobuf.InvalidProtocolBufferException e) {
          parsedMessage = (org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device) e.getUnfinishedMessage();
          throw e.unwrapIOException();
        } finally {
          if (parsedMessage != null) {
            mergeFrom(parsedMessage);
          }
        }
        return this;
      }

      private java.lang.Object type_ = "";
      /**
       * <code>string type = 1[json_name = "type"];</code>
       * @return The type.
       */
      public java.lang.String getType() {
        java.lang.Object ref = type_;
        if (!(ref instanceof java.lang.String)) {
          com.google.protobuf.ByteString bs =
              (com.google.protobuf.ByteString) ref;
          java.lang.String s = bs.toStringUtf8();
          type_ = s;
          return s;
        } else {
          return (java.lang.String) ref;
        }
      }
      /**
       * <code>string type = 1[json_name = "type"];</code>
       * @return The bytes for type.
       */
      public com.google.protobuf.ByteString
          getTypeBytes() {
        java.lang.Object ref = type_;
        if (ref instanceof String) {
          com.google.protobuf.ByteString b = 
              com.google.protobuf.ByteString.copyFromUtf8(
                  (java.lang.String) ref);
          type_ = b;
          return b;
        } else {
          return (com.google.protobuf.ByteString) ref;
        }
      }
      /**
       * <code>string type = 1[json_name = "type"];</code>
       * @param value The type to set.
       * @return This builder for chaining.
       */
      public Builder setType(
          java.lang.String value) {
        if (value == null) {
    throw new NullPointerException();
  }
  
        type_ = value;
        onChanged();
        return this;
      }
      /**
       * <code>string type = 1[json_name = "type"];</code>
       * @return This builder for chaining.
       */
      public Builder clearType() {
        
        type_ = getDefaultInstance().getType();
        onChanged();
        return this;
      }
      /**
       * <code>string type = 1[json_name = "type"];</code>
       * @param value The bytes for type to set.
       * @return This builder for chaining.
       */
      public Builder setTypeBytes(
          com.google.protobuf.ByteString value) {
        if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
        
        type_ = value;
        onChanged();
        return this;
      }
      @java.lang.Override
      public final Builder setUnknownFields(
          final com.google.protobuf.UnknownFieldSet unknownFields) {
        return super.setUnknownFields(unknownFields);
      }

      @java.lang.Override
      public final Builder mergeUnknownFields(
          final com.google.protobuf.UnknownFieldSet unknownFields) {
        return super.mergeUnknownFields(unknownFields);
      }


      // @@protoc_insertion_point(builder_scope:syft_proto.types.torch.v1.Device)
    }

    // @@protoc_insertion_point(class_scope:syft_proto.types.torch.v1.Device)
    private static final org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device DEFAULT_INSTANCE;
    static {
      DEFAULT_INSTANCE = new org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device();
    }

    public static org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device getDefaultInstance() {
      return DEFAULT_INSTANCE;
    }

    private static final com.google.protobuf.Parser<Device>
        PARSER = new com.google.protobuf.AbstractParser<Device>() {
      @java.lang.Override
      public Device parsePartialFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws com.google.protobuf.InvalidProtocolBufferException {
        return new Device(input, extensionRegistry);
      }
    };

    public static com.google.protobuf.Parser<Device> parser() {
      return PARSER;
    }

    @java.lang.Override
    public com.google.protobuf.Parser<Device> getParserForType() {
      return PARSER;
    }

    @java.lang.Override
    public org.openmined.syftproto.types.torch.v1.DeviceOuterClass.Device getDefaultInstanceForType() {
      return DEFAULT_INSTANCE;
    }

  }

  private static final com.google.protobuf.Descriptors.Descriptor
    internal_static_syft_proto_types_torch_v1_Device_descriptor;
  private static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_syft_proto_types_torch_v1_Device_fieldAccessorTable;

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n&syft_proto/types/torch/v1/device.proto" +
      "\022\031syft_proto.types.torch.v1\"\034\n\006Device\022\022\n" +
      "\004type\030\001 \001(\tR\004typeB(\n&org.openmined.syftp" +
      "roto.types.torch.v1b\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        });
    internal_static_syft_proto_types_torch_v1_Device_descriptor =
      getDescriptor().getMessageTypes().get(0);
    internal_static_syft_proto_types_torch_v1_Device_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_syft_proto_types_torch_v1_Device_descriptor,
        new java.lang.String[] { "Type", });
  }

  // @@protoc_insertion_point(outer_class_scope)
}
