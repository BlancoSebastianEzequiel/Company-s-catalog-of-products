const fieldsState = {
  first_name: '',
  last_name: '',
  user_name: '',
  email: '',
  password: '',
  type: 'client',
  passConfirmation: ''
}
const fields = [
  {
    placeholder: 'harry',
    fieldName: 'first_name',
    title: 'First name',
    type: 'text'
  },
  {
    placeholder: 'potter',
    fieldName: 'last_name',
    title: 'Last name',
    type: 'text'
  },
  {
    placeholder: 'harry_potter',
    fieldName: 'user_name',
    title: 'User name',
    type: 'text'
  },
  {
    placeholder: 'harry_potter@gmail.com',
    fieldName: 'email',
    title: 'Email',
    type: 'email'
  },
  {
    placeholder: '12345',
    fieldName: 'password',
    title: 'Password',
    type: 'password'
  },
  {
    placeholder: '12345',
    fieldName: 'passConfirmation',
    title: 'Confirm password',
    type: 'password'
  }
]

const data = {
  'fields': fields,
  'fieldsState': fieldsState
}

export default data
