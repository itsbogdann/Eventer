var optionClassSubmit = {
    success: showResponse
}
//var moment=require('moment');
$(document).ready(function() {
    var username = sessionStorage.getItem("username");
    if (username != 0 && username != null) {
        $("#loginLabelUser").html(username);
        $("#logOutLabel").hide();
        $("#logInLabel").show();
    }
    bindEvents(optionClassSubmit);
    $("#classesShow").show();
    $(".results-search").html("");
    for (var i = 0; i < 10; i++) {
        var banner = $("#template>.banner").clone();
        banner.find(".className").html("ComputerScience");
        banner.find(".unieversityName").html("Politehnica");
        //banner.css("display: block");
        $(".results-search").append(banner);
    }
})

var bindEvents = function(optionClassSubmit) {
    // $('#calendar').clndr();
  //  workWithCalendar();
    $('#searchForm').ajaxForm(optionClassSubmit);
    $('#searchForm').submit(function() {
        return false;
    })
    $("#template").hide();
    $("logOut").click(function() {
        sessionStorage.setItem("username", 0);
        $(window.location).attr("href", "index.html");
    })
    fillSubjectList();
    fillUnivesityList();
    $("#myClassShow").hide();
    $("#myClassesButton").click(function() {
        $("#myClassShow").show();
        $("#classesShow").hide();
    });
    $("#allClassesButton").click(function() {
        $("#myClassShow").hide();
        $("#classesShow").show();
    });
}

function fillSubjectList() {
    subjects = ["Computer Science", "Psychology", "Arts", "Electrical Engineering"];
    for (var i = 0; i < subjects.length; i++) {
        var new_div = $("<option value='" + subjects[i] + "'></option>");
        $("#classSearch").append(new_div);
    }
}

function fillUnivesityList() {
    subjects = ["MIT", "Politehnica", "UCL", "Imperial"];
    for (var i = 0; i < subjects.length; i++) {
        var new_div = $("<option value='" + subjects[i] + "'></option>");
        $("#universitySearch").append(new_div);
    }
}

function showResponse(data) {
    console.log(data);
}

// function workWithCalendar() {
//     var currentMonth = moment().format('YYYY-MM');
//     var nextMonth = moment().add('month', 1).format('YYYY-MM');
//     var events = [{
//         date: currentMonth + '-' + '10',
//         title: 'Persian Kitten Auction',
//         location: 'Center for Beautiful Cats'
//     }, {
//         date: currentMonth + '-' + '19',
//         title: 'Cat Frisbee',
//         location: 'Jefferson Park'
//     }, {
//         date: currentMonth + '-' + '23',
//         title: 'Kitten Demonstration',
//         location: 'Center for Beautiful Cats'
//     }, {
//         date: nextMonth + '-' + '07',
//         title: 'Small Cat Photo Session',
//         location: 'Center for Cat Photography'
//     }];
//
//     $('#mini-clndr').clndr({
//         template: $('#calendar-template').html(),
//         events: events,
//         clickEvents: {
//             click: function(target) {
//                 if (target.events.length) {
//                     var daysContainer = $('#mini-clndr').find('.days-container');
//                     daysContainer.toggleClass('show-events', true);
//                     $('#mini-clndr').find('.x-button').click(function() {
//                         daysContainer.toggleClass('show-events', false);
//                     });
//                 }
//             }
//         },
//         adjacentDaysChangeMonth: true
//     });
// }