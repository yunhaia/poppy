# Copyright (c) 2015 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from poppy.transport.validators import schema_base


class DomainMigrationServiceSchema(schema_base.SchemaBase):

    '''JSON Schema validation for /admin/provider/akamai/service'''

    schema = {
        'domain_migration': {
            'POST': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'project_id': {
                        'type': 'string',
                        'required': True
                    },
                    'service_id': {
                        'type': 'string',
                        'required': True
                    },
                    'domain_name': {
                        'type': 'string',
                        'required': True,
                        'minLength': 3,
                        'maxLength': 253
                    },
                    'new_cert': {
                        'type': 'string',
                        'required': True
                    },
                    'cert_status': {
                        'type': 'string',
                        'required': False,
                        'enum': ['create_in_progress', 'deployed']
                    }
                }
            }
        }
    }
