function doGet(e) {
  var ms = SpreadsheetApp.getActive().getSheetByName("Messages");  
  var count = ms.getLastRow()-1;
  
  if("tenho" in e.parameter){
    var tenho = e.parameter.tenho;
    return getMessages(ms, count - tenho);
  }else{
    return getMessages(ms, count);
  }
}  

function doPost(e) {
  var json = JSON.parse(e.postData.contents);
  
  if(("message" in json) && ("author" in json)){
    var ms = SpreadsheetApp.getActive().getSheetByName("Messages");
    ms.appendRow([json.message, json.author, new Date()]);
    ms.getRange(2,1,ms.getLastRow()-1, 3).sort({column: 3, ascending: false});
  }

  var contentService = ContentService.createTextOutput(JSON.stringify({
    "message":"ok"
  }));

  contentService.setHeader('Access-Control-Allow-Origin', '*');
  contentService.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  contentService.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  contentService.setMimeType(ContentService.MimeType.JSON);
  return contentService;
}

function getMessages(ms, k){
  var data = [];
  if(k>0){
    data = ms.getRange(2,1,k, 3).getValues();
  }
  var contentService = ContentService.createTextOutput(JSON.stringify(data));
  contentService.setMimeType(ContentService.MimeType.JSON);
  return contentService;
}
