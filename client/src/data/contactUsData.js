const fieldsState = {
  email: '',
  password: '',
  subject: '',
  message: ''
}
const fields = [
  {
    placeholder: 'something@example.com',
    fieldName: 'email',
    title: 'Email',
    type: 'email'
  },
  {
    placeholder: '1234',
    fieldName: 'password',
    title: 'Password',
    type: 'password'
  },
  {
    placeholder: 'Discount',
    fieldName: 'subject',
    title: 'Subject',
    type: 'text'
  },
  {
    placeholder: 'Hello! my name is James Potte and i would like to....',
    fieldName: 'message',
    title: 'Message',
    type: 'text'
  }
]

const data = {
  'fields': fields,
  'fieldsState': fieldsState
}

export default data
