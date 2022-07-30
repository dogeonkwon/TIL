const express = require('express')  // express를 다운 받았기 때문에 가져올 수 있다.
const app = express()   // 새로운 앱 만들기
const port = 5000   // 3000, 4000 해도 상관없음

const mongoose = require('mongoose')

// <password> 자리에 비밀번호를 입력해야 한다.
mongoose.connect('mongodb+srv://dogeon:Rnjs68427!@boilerplate.2ctgbnl.mongodb.net/?retryWrites=true&w=majority', {
    useNewUrlParser: true, useUnifiedTopology: true
}).then(() => console.log('MongoDB Connected..'))	// 연결이 잘 되었을 때 출력
  .catch(err => console.log('err'))		// 잘 되지 않았을 때 출력

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})