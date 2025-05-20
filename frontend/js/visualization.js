// Fetch the sample incident logs from the data folder (for a static demo)
fetch('../data/sample_incidents.json')
  .then(response => response.json())
  .then(data => {
    // For a static demo, we assume the events are pre-classified.
    // If not, similar classification logic using JavaScript could be applied.
    const counts = {};
    data.forEach(event => {
      const comp = event.component || "Unknown";
      counts[comp] = (counts[comp] || 0) + 1;
    });
    const labels = Object.keys(counts);
    const values = Object.values(counts);
    
    const ctx = document.getElementById('incidentChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Number of Incidents',
          data: values,
          backgroundColor: 'rgba(153, 102, 255, 0.7)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  .catch(error => console.error('Error fetching sample incidents:', error));
