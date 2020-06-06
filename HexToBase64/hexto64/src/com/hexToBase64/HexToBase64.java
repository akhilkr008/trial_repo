package com.hexToBase64;
import java.io.*;
import java.util.*;

import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.Hex;
public class HexToBase64 {
	
	public static void main(String[] args) throws DecoderException {
		String hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
		char[] charArray = hexString.toCharArray();
		byte[] decodedHex = Hex.decodeHex(charArray);
		String base64Array = Base64.encodeBase64String(decodedHex);
		System.out.println(base64Array);

	}

}
	