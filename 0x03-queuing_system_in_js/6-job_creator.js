import kue from 'kue';

const data = {
  phoneNumber: '01006044591',
  message: 'Hello, Abdo',
};

const push_notification_code = kue.createQueue();
const smsJob = push_notification_code.create('sms', data).save((err) => {
  if (!err) {
    console.log('Notification job created:', smsJob.id);
  }
});

smsJob.on('complete', (result) => {
  console.log('Notification job completed');
});

smsJob.on('failed', () => {
  console.log('Notification job failed');
});
