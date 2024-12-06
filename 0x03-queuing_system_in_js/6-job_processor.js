import kue from 'kue';

const queue = kue.createQueue();

queue.process('sms', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, done);
});

function sendNotification(phoneNumber, message, done) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  done();
}
