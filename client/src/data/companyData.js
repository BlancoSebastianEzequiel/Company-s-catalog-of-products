const fieldsState = {
  quantity_of_employees: '',
  address: '',
  capabilities: '',
  mission: '',
  vision: '',
  values: ''
}
const fields = [
  {
    placeholder: '200',
    fieldName: 'quantity_of_employees',
    title: 'Quantity of employees',
    type: 'text'
  },
  {
    placeholder: 'Ing Enrique Butty 275, C1001AFA CABA',
    fieldName: 'address',
    title: 'Address',
    type: 'text'
  },
  {
    placeholder: 'Blockchain',
    fieldName: 'capabilities',
    title: 'Capabilities',
    type: 'text'
  },
  {
    placeholder: 'to lead in the creation...',
    fieldName: 'mission',
    title: 'mission',
    type: 'text'
  },
  {
    placeholder: 'to be the world’s most successful...',
    fieldName: 'vission',
    title: 'Vission',
    type: 'text'
  },
  {
    placeholder: 'Dedication to every clients success',
    fieldName: 'values',
    title: 'Values',
    type: 'text'
  }
]

const data = {
  'fields': fields,
  'fieldsState': fieldsState
}

export default data
