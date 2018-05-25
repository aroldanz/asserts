import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

class GenericExceptionsOpen{
    public static void main(String args[]){
      try{
          int a[]=new int[7];
          a[4]=30/0;
          System.out.println("First print statement in try block");
          if (a[0] > 200) {
              System.out.println("Big num");
          } else  if (a[0] < 100){
              System.out.println("Small num");
          }
      }

      MessageDigest messageDigest, messageDigest2;
      messageDigest = MessageDigest.getInstance("MD5");
      messageDigest.update(data.getBytes());
      byte[] messageDigestMD5 = messageDigest.digest();
      messageDigest2 = MessageDigest.getInstance("SHA-1");
      messageDigest2.update(data.getBytes());
      byte[] messageDigestSHA1 = messageDigest2.digest();

      Cipher des = Cipher.getInstance("DES");
      des.init(Cipher.ENCRYPT_MODE, secretKeySpec);
      byte[] encrypted = des.doFinal(input.getBytes("UTF-8"));

      catch(ArithmeticException e){
         System.out.println("Warning: ArithmeticException");
      }
      catch(ArrayIndexOutOfBoundsException e){
         System.out.println("Warning: ArrayIndexOutOfBoundsException");
      }
      catch(Exception e){
         System.out.println("Warning: Some Other exception");
      }
    try {
        System.out.println("Out of try-catch block...");
    }
   catch(Exception e){
         e.printStackTrace();
      }
    }
   }