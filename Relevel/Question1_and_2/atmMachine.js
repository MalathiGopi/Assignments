class ATM {
    constructor(action, atmObj) {
      this.action = action;
      this.atmObj = atmObj;

      //check the Action and redirect into respective function
      if (this.action === 'BALANCE'){
        this.getbalance(atmObj.pin)
      }else if (this.action === 'WITHDRAW_CASH'){
        this.withdrawCash(atmObj.pin,atmObj.balance)
      }else{
        console.log("Invalid Option")
      }
    }

    //Display the balance if pin is correct
    getbalance(pin) {
        if (this.checkPin(pin)){
            console.log(this.balance)
        }else{
            console.error('Incorrect pin !')
        }
        
    }

    //Function to check the pin
    checkPin(pin){
        let pinStatus=false
        console.log('checkpin')
        if (pin === this.atmObj.pin){
            pinStatus=true
        }else{
            pinStatus=false
        }
        return pinStatus
    }

    //  question -2 
    //Function to withdraw the cash if balance if sufficient
    withdrawCash(pin, withdrawAmount){
        if (this.checkPin(pin)){
            if (this.balance >= withdrawAmount){
                console.log(`Please collect your cash

                Your balance is ${this.balance} Rupees`)
            }else{
                console.error('Incorrect pin !')
            }
        }else{
            console.error('Insufficient balance !')
        }

    }
  }

const obj1 = new ATM('BALANCE', {

    pin: 1234,
  
    balance: 1000
  
  });

  const obj2 = new ATM('WITHDRAW_CASH', {

    pin: 12345,
  
    balance: 1000
  
  });