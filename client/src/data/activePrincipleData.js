const fieldsState = {
  code: '',
  name: '',
  description: ''
}

const fields = [
  {
    placeholder: '200',
    fieldName: 'code',
    title: 'Code',
    type: 'text'
  },
  {
    placeholder: 'paracetamol',
    fieldName: 'name',
    title: 'Name',
    type: 'text'
  },
  {
    placeholder: 'analgésicos y antiinflamatorios',
    fieldName: 'description',
    title: 'Description',
    type: 'text'
  }
]

const data = {
  'fields': fields,
  'fieldsState': fieldsState
}

export default data
