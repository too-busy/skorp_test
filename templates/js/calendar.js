// calendar.js
document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    events: '/arbeitsplan/entries/' // Ändern Sie den Pfad entsprechend Ihrer URLs
  });

  calendar.render();
});
