const fieldsState = {
  code: '',
  name: '',
  description: '',
  images: [],
  size: '',
  active_principle: ''
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
  },
  {
    placeholder: '',
    fieldName: 'images',
    title: 'Images',
    type: 'file'
  },
  {
    placeholder: '70ml',
    fieldName: 'size',
    title: 'Size',
    type: 'text'
  },
  {
    placeholder: '300',
    fieldName: 'active_principle',
    title: 'Active principle code',
    type: 'text'
  }
]

const fieldsStateSearch = {
  code: '',
  name: '',
  description: '',
  size: '',
  active_principle: ''
}

const searchFields = [
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
  },
  {
    placeholder: '70ml',
    fieldName: 'size',
    title: 'Size',
    type: 'text'
  },
  {
    placeholder: '300',
    fieldName: 'active_principle',
    title: 'Active principle code',
    type: 'text'
  }
]

const data = {
  'fields': fields,
  'fieldsState': fieldsState,
  'searchFields': searchFields,
  'fieldsStateSearch': fieldsStateSearch
}

export default data
