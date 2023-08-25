const moment = require('moment');
const crypto = require('crypto');
const timestamp = moment().valueOf();
console.log(timestamp);


// const secretKey = 'a7ac23fa-4242-591d-ad0e-81637b0aafc6'
// const ApiKey = '2142aec0-4188-11ee-82bc-c1fe7802e12d'


secretKey = 'a7ac23fa-4242-591d-ad0e-81637b0aafc6'
ApiKey = '2142aec0-4188-11ee-82bc-c1fe7802e12d'
const path = 'oapi/v1/trade/market/orderbook'

function createSignature(secretKey, fullPath, requestMethod, requestData = null) {
    const timestamp = moment().valueOf();
    let msg = `${requestMethod.toUpperCase()}\n${fullPath}\n${timestamp}`;
  
    if (requestData) {
      const base64Encoded = Buffer.from(JSON.stringify(requestData)).toString('base64');
      msg += `\n${base64Encoded}`;
    }
  
    const signedKey = crypto
      .createHmac('sha256', secretKey)
      .update(msg)
      .digest('hex');
  
    return [signedKey, timestamp];
  }
  

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("x-api-key", "2142aec0-4188-11ee-82bc-c1fe7802e12d");
myHeaders.append("x-secret-key", "a7ac23fa-4242-591d-ad0e-81637b0aafc6");
myHeaders.append("x-timestamp", "1692905733624");
myHeaders.append("x-signature", "bfb93c6cda7ffd4b2dbfdc87ff83ddb6eb3539a10208f2828105d04cf0901664");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

try {
  
  fetch("https://api.ok-ex.io/oapi/v1/trade/market/history", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
} catch (error) {
  console.log(error);
}


console.log(createSignature(secretKey,path,'get'));
