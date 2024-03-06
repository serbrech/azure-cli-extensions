# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "automation runtime-environment package create",
)
class Create(AAZCommand):
    """Create the package identified by package name.

    :example: Create Runtime Environment Package
        az automation runtime-environment package create -g rg--automation-account-name myAutomationAccount --runtime-environment-name rt --name rt-package --uri https://teststorage.blob.core.windows.net/mycontainer/MyModule.zip --content-version 1.0.0.0
    """

    _aaz_info = {
        "version": "2023-05-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.automation/automationaccounts/{}/runtimeenvironments/{}/packages/{}", "2023-05-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.automation_account_name = AAZStrArg(
            options=["--account", "--automation-account-name"],
            help="The name of the automation account.",
            required=True,
        )
        _args_schema.package_name = AAZStrArg(
            options=["-n", "--name", "--package-name"],
            help="The name of Package.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.runtime_environment_name = AAZStrArg(
            options=["--environment", "--runtime-environment-name"],
            help="The name of the Runtime Environment.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z-_0-9]*$",
            ),
        )

        # define Arg Group "ContentLink"

        _args_schema = cls._args_schema
        _args_schema.content_hash = AAZObjectArg(
            options=["--content-hash"],
            arg_group="ContentLink",
            help="Gets or sets the hash of content.",
        )
        _args_schema.content_uri = AAZStrArg(
            options=["--uri", "--content-uri"],
            arg_group="ContentLink",
            help="Gets or sets the uri of content.",
        )
        _args_schema.content_version = AAZStrArg(
            options=["--content-version"],
            arg_group="ContentLink",
            help="Gets or sets the version of the content.",
        )

        content_hash = cls._args_schema.content_hash
        content_hash.algorithm = AAZStrArg(
            options=["algorithm"],
            help="Gets or sets the content hash algorithm used to hash the content.",
            required=True,
        )
        content_hash.value = AAZStrArg(
            options=["value"],
            help="Gets or sets expected hash value of the content.",
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.all_of = AAZObjectArg(
            options=["--all-of"],
            arg_group="Parameters",
            help="The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'",
        )

        all_of = cls._args_schema.all_of
        all_of.location = AAZResourceLocationArg(
            options=["l", "location"],
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        all_of.tags = AAZDictArg(
            options=["tags"],
            help="Resource tags.",
        )

        tags = cls._args_schema.all_of.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PackageCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PackageCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runtimeEnvironments/{runtimeEnvironmentName}/packages/{packageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "automationAccountName", self.ctx.args.automation_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packageName", self.ctx.args.package_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "runtimeEnvironmentName", self.ctx.args.runtime_environment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-05-15-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("allOf", AAZObjectType, ".all_of")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            all_of = _builder.get(".allOf")
            if all_of is not None:
                all_of.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
                all_of.set_prop("tags", AAZDictType, ".tags")

            tags = _builder.get(".allOf.tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("contentLink", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            content_link = _builder.get(".properties.contentLink")
            if content_link is not None:
                content_link.set_prop("contentHash", AAZObjectType, ".content_hash")
                content_link.set_prop("uri", AAZStrType, ".content_uri")
                content_link.set_prop("version", AAZStrType, ".content_version")

            content_hash = _builder.get(".properties.contentLink.contentHash")
            if content_hash is not None:
                content_hash.set_prop("algorithm", AAZStrType, ".algorithm", typ_kwargs={"flags": {"required": True}})
                content_hash.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _CreateHelper._build_schema_system_data_read(_schema_on_200_201.system_data)
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.all_of = AAZObjectType(
                serialized_name="allOf",
                flags={"read_only": True},
            )
            _CreateHelper._build_schema_system_data_read(properties.all_of)
            properties.content_link = AAZObjectType(
                serialized_name="contentLink",
            )
            properties.default = AAZBoolType()
            properties.error = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.size_in_bytes = AAZIntType(
                serialized_name="sizeInBytes",
            )
            properties.version = AAZStrType()

            content_link = cls._schema_on_200_201.properties.content_link
            content_link.content_hash = AAZObjectType(
                serialized_name="contentHash",
            )
            content_link.uri = AAZStrType()
            content_link.version = AAZStrType()

            content_hash = cls._schema_on_200_201.properties.content_link.content_hash
            content_hash.algorithm = AAZStrType(
                flags={"required": True},
            )
            content_hash.value = AAZStrType(
                flags={"required": True},
            )

            error = cls._schema_on_200_201.properties.error
            error.code = AAZStrType()
            error.message = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["Create"]