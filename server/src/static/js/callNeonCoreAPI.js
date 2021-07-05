
const NeonCoreEndpoint ="https://mx-demo-wjrnu3p4ya-uc.a.run.app";
const NeonDashboardURL = "https://dashboard.joinneon.com";
const NeonCoreHeader = {
  'X-NEON-TOKEN': "SAMPLE_API_KEY"
}

window.addEventListener('message', process_payment_token, false);
var neonPaymentWindow = '';
var pmt_token;
function process_payment_token(evt) {
  if (evt.origin !== NeonCoreEndpoint) {
    console.log('BAD SOURCE');
  } else {
    console.log(evt);
    console.log('TRIGGERED SOME EVVENT', evt.data)
    console.log("ORIGIN: ", evt.origin);
    if (evt.data.hasOwnProperty("payment_token")) {
      var pmt_token_query_param = new URLSearchParams(evt.data).toString();
      console.log("PAYMENT TOKEN: ", evt.data["payment_token"]);
      neonPaymentWindow.close();
      window.location.href='/finish_order?' + pmt_token_query_param;
    }
  }

}

 function integrate_with_neon() {
   const stockx_data = {
     eligibility: true,
     original_item_price: 274.00,
     original_item_name: "Jordan 11 Retros",
     original_item_size: "10M",
     manufactuer_part_number: "Sku 378039 011",
     email: "jackie@joinneon.com"
   }
   var queryString = $.param(stockx_data);

   // Make POST call to request for a session token for passed parameters using NEON API TOKEN.
   const createInitiateNeonEndpoint = NeonCoreEndpoint + '/core/createInitiateNeonSession?'+queryString;

   $.ajax({
     url: createInitiateNeonEndpoint,
     type: 'POST',
     dataType: 'json',
     data: stockx_data,
     headers: NeonCoreHeader,
     success: function(result) {
       const initiateNeonEndpoint = NeonCoreEndpoint + '/core/initiateNeon/'+result['session_token'];
       console.log('Openning new window: ', initiateNeonEndpoint);
       neonPaymentWindow = window.open(initiateNeonEndpoint,"","resizable=no,width=420,height=520");
       console.log(result);
     },
     error: function(error) {
       console.log(error)
     }
   });


   // if (neonPaymentWindow.document.queryselector('body').innerText.indexOf('payment_token_ID') > -1) {
   //   neonPaymentWindow.close();
   // }
  //  neonPaymentWindow.onbeforeunload = function () {
  //     // processing event here
  //     alert("new window closed");
  // }
 }


 function getParameterByName(name, url = window.location.href) {
       // Use regex to parse query parameters
      name = name.replace(/[\[\]]/g, '\\$&');
      var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
          results = regex.exec(url);
      if (!results) return null;
      if (!results[2]) return '';
      return decodeURIComponent(results[2].replace(/\+/g, ' '));
  }

 async function call_api_with_address(params) {
  if (document.getElementById('stockx_continue').innerHTML != 'Confirm Purchase'){
    document.getElementById('stockx_continue').innerHTML = 'Confirm Purchase';
    document.getElementById('addy').style.display = 'none';
    document.getElementById('confirm').style.display = '';
  } else if (document.getElementById('stockx_continue').innerHTML == 'Confirm Purchase') {
    // Clicking Confirm purchase should call POST to the complete txn endpoint.
    const urlSearchParams = new URLSearchParams(window.location.search);
    const params = Object.fromEntries(urlSearchParams.entries());
    console.log('All extracted query parameters: ', params);
    const pmt_token = params['payment_token'];
    console.log('Extracted payment_token: ', pmt_token);
    const completetxn_endpoint = NeonCoreEndpoint + '/core/complete_transaction/' + pmt_token;
    console.log('Fetching POST ', completetxn_endpoint);
    let response = await fetch(completetxn_endpoint, {
      method: 'post',
      body: null
    });
    let returned_txn_json = await response.json();
    alert("Payment token " + pmt_token + " has been submitted to complete transaction.\n\n");//Response from Neon Core API:" + JSON.stringify(returned_txn_json));
    console.log(returned_txn_json);
    window.location.href=NeonDashboardURL;
  }
 }

$(document).ready(function() {
  const stockx_data = {
    eligibility: true,
    original_item_price: 274.00,
    original_item_name: "Jordan 11 Retros",
    original_item_size: "10M",
    manufactuer_part_number: "Sku 378039 011",
    email: "jackie@joinneon.com"
  }
  var queryString = $.param(stockx_data);

  // First validate parameters using Neon Core API validate endpoint
  const validateEndpoint = NeonCoreEndpoint + "/core/validate?" + queryString;
  console.log("Calling validation endpoint:  GET ", validateEndpoint);
  var validation_response = fetch(validateEndpoint, {
    headers: NeonCoreHeader,
    mode: 'no-cors'
  })
  .then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data);
  });
})
