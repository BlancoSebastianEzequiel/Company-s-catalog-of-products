const fieldsState = {
  title: '',
  description: ''
}
const fields = [
  {
    placeholder: 'Register',
    fieldName: 'title',
    title: 'title',
    type: 'text'
  },
  {
    placeholder: 'To register you have to....',
    fieldName: 'description',
    title: 'Desctription',
    type: 'text'
  }
]

const data = {
  'fields': fields,
  'fieldsState': fieldsState
}

export default data
