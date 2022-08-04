// Working Perfect Code

// $(document).ready(function() {

// 	$('#submitButton').on('click', function(event) {

// 		event.preventDefault();

// 		var formData = new FormData($('#myform')[0]);
        
//         console.log(formData);
        
// 		$.ajax({
// 			xhr : function() {
// 				var xhr = new window.XMLHttpRequest();

// 				xhr.upload.addEventListener('progress', function(e) {

// 					if (e.lengthComputable) {

// 						console.log('Bytes Loaded: ' + e.loaded);
// 						console.log('Total Size: ' + e.total);
// 						console.log('Percentage Uploaded: ' + (e.loaded / e.total))

// 						var percent = Math.round((e.loaded / e.total) * 100);

// 						$('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');

// 					}

// 				});

// 				return xhr;
// 			},
// 			type : 'POST',
// 			url : '/download',
// 			data : formData,
// 			processData : false,
// 			contentType : false,
// 			success : function() {
// 				alert('File uploaded!');
// 			}
// 		});

// 	});

// });




// function loaderHide() {
//     var x = document.getElementById("loader");
//     if (x.style.display === "none") {
//       x.style.display = "block";
//     } else {
//       x.style.display = "none";
//     }
//   } 


///// MP3 /////
$(document).ready(function() {

	$("#loader").hide(); 
	$('#mp3').on('click', function(event) {
		
		var vid_url = document.getElementById("vid_url").value;
		var initial_time = document.getElementById("initial_time").value;
		var final_time = document.getElementById("final_time").value;
		
		if (vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else if (initial_time == "" && final_time == "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/audio';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url != "") {
			alert("Sorry! MP3 format is currently unavailable");
			return false;
		}
		else if (initial_time != "" && final_time != "" && vid_url == "") {
			alert("Field can't be empty!");
			return false;
		}
		else {
			alert("Field can't be empty!")
			return false;
		}

	});
});

///// Normal ///////
$(document).ready(function() {

	$("#loader").hide(); 
	$('#normal').on('click', function(event) {
		
		var vid_url = document.getElementById("vid_url").value;
		var initial_time = document.getElementById("initial_time").value;
		var final_time = document.getElementById("final_time").value;
		
		if (vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else if (initial_time == "" && final_time == "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/low';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/crop_vid';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else {
			alert("Field can't be empty!")
			return false;
		}

	});
});

/////// best ////////
$(document).ready(function() {

	$("#loader").hide(); 
	$('#best').on('click', function(event) {
		
		var vid_url = document.getElementById("vid_url").value;
		var initial_time = document.getElementById("initial_time").value;
		var final_time = document.getElementById("final_time").value;
		
		if (vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else if (initial_time == "" && final_time == "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/best';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/crop_vid';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else {
			alert("Field can't be empty!")
			return false;
		}

	});
});

/////// vbest ////////
$(document).ready(function() {

	$("#loader").hide(); 
	$('#vbest').on('click', function(event) {
		
		var vid_url = document.getElementById("vid_url").value;
		var initial_time = document.getElementById("initial_time").value;
		var final_time = document.getElementById("final_time").value;
		
		if (vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else if (initial_time == "" && final_time == "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/vbest';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/crop_vid';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url == "") {
			alert("Field can't be empty!")
			return false;
		}
		else {
			alert("Field can't be empty!")
			return false;
		}

	});
});


////////// Download ////////
$(document).ready(function() {

	$("#loader").hide(); 
	$('#download_bt').on('click', function(event) {
		
		var vid_url = document.getElementById("vid_url").value;
		var initial_time = document.getElementById("initial_time").value;
		var final_time = document.getElementById("final_time").value;
		
		if (vid_url == "") {
			alert("Field can't be empty!");
			return false;
		}
		else if (initial_time == "" && final_time == "" && vid_url != "") {
			return false;
		}
		else if (initial_time != "" && final_time != "" && vid_url != "") {
			$("#loader").show();
			document.getElementById('myform').action = '/crop_vid';
			document.getElementById('myform').submit();
		}
		else if (initial_time != "" && final_time != "" && vid_url == "") {
			alert("Field can't be empty!");
			return false;
		}
		else {
			alert("Field can't be empty!");
			return false;
		}

	});
});


////////// Scrape button  /////////
$(document).ready(function() {

	$("#loader-2").hide(); 
	$('#scrape_bt').on('click', function() {
		
		var user_kw = document.getElementById("user_keyw").value;
		
		if (user_kw == "") {
			alert("Field can't be empty!");
			return false;
		}
		else if (user_kw != "") {
			// $("#loader").show();
			console.log("Kch aya!");
			$("#loader-2").show();
			document.getElementById("scrapeform").action = '/scrape';
			document.getElementById("scrapeform").submit();
		}
		else {
			alert("Field can't be empty!")
			return false;
		}

	});
});










