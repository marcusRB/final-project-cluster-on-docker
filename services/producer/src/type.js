const avro = require('avsc');

const avroSchema = {
  name: 'SaleType',
  type: 'record',
  fields: [
    {
      name: 'saleDate',
      type: {
        type: 'long',
        logicalType: 'timestamp-millis'
      }
    },
    {
      name: 'total',
      type: 'double'
    },
    {
      name: 'city',
      type: 'string'
    },
    {
      name: 'country',
      type: 'string'
    },
    {
      name: 'latitude',
      type: 'float'
    },
    {
      name: 'longitude',
      type: 'float'
    }
  ]
};

const type = avro.parse(avroSchema)

module.exports = type;