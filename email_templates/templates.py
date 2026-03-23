
def login_alert(time, user_name):
    subject = "Security Alert: Unusual Login Detected"
    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Security Alert - Account Login Detected</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header with Warning -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); padding: 40px 30px; text-align: center;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <div style="width: 70px; height: 70px; background-color: rgba(255,255,255,0.2); border-radius: 50%; display: inline-block; text-align: center; line-height: 70px; margin-bottom: 20px;">
                                            <span style="font-size: 40px; color: #ffffff;">⚠️</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 28px; font-weight: 600;">Security Alert</h1>
                                        <p style="margin: 0; color: #ffffff; font-size: 16px; opacity: 0.95;">Unusual login activity detected</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Hello <strong>{user_name}</strong>,
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                We detected a login to your account that appears slightly unusual. This could be a routine login from a new location or device, but we wanted to make sure it was you.
                            </p>

                            <!-- Critical Alert Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #856404; font-size: 15px; font-weight: 600;">
                                            ⚠️ Action Required - Review This Login
                                        </p>
                                        <p style="margin: 0; color: #856404; font-size: 14px; line-height: 1.6;">
                                            This login attempt has been flagged due to unusual patterns. Please verify that this was you.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Time Display -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8f9fa; border-left: 4px solid #ff6b6b; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #495057; font-size: 14px; font-weight: 600;">Login Time:</p>
                                        <p style="margin: 0; color: #212529; font-size: 18px; font-weight: 600;">{time}</p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Security Warning -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8d7da; border-left: 4px solid #dc3545; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #721c24; font-size: 15px; font-weight: 600;">
                                            🔒 If This Wasn't You
                                        </p>
                                        <p style="margin: 0; color: #721c24; font-size: 14px; line-height: 1.6;">
                                            Please <strong>change your password immediately</strong> to secure your account. We recommend using a strong, unique password and enabling two-factor authentication for added security.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Security Tips -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #e7f3ff; border-left: 4px solid #0066cc; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #004085; font-size: 14px; font-weight: 600;">
                                            🛡️ Security Recommendations:
                                        </p>
                                        <ul style="margin: 0; padding-left: 20px; color: #004085; font-size: 14px; line-height: 1.8;">
                                            <li>Use a strong, unique password for your account</li>
                                            <li>Never share your password with anyone</li>
                                        </ul>
                                    </td>
                                </tr>
                            </table>

                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                If you have any questions or need assistance securing your account, our support team is available 24/7 to help you.
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <p style="margin: 0 0 10px 0; color: #667eea; font-weight: 600; font-size: 18px;">HireNest Team Platform</p>
                                        <p style="margin: 0 0 15px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            © 2026 HireNest Team. All rights reserved.<br>
                                            Your security is our top priority.
                                        </p>
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tr>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Privacy Policy</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Terms of Service</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Support</a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="margin: 15px 0 0 0; color: #adb5bd; font-size: 12px;">
                                            123 Business Street, Suite 100, City, State 12345<br>
                                            This is an automated security alert. Please do not reply to this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                </table>

                <!-- Mobile-only text -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 20px auto 0;">
                    <tr>
                        <td align="center" style="color: #999999; font-size: 12px; padding: 0 20px;">
                            You received this security alert because unusual activity was detected on your HireNest Team account.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""
    templets = {
        "subject": subject,
        "body": body
    }
    return templets


def verify_email_templetes(url, email):
    subject = "Account Verification Alert"

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Verify Your Email Address</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <div style="width: 80px; height: 80px; background-color: rgba(255,255,255,0.2); border-radius: 50%; display: inline-block; text-align: center; line-height: 80px; margin-bottom: 20px;">
                                            <span style="font-size: 45px; color: #ffffff;">✉️</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 28px; font-weight: 600;">Verify Your Email</h1>
                                        <p style="margin: 0; color: #ffffff; font-size: 16px; opacity: 0.95;">Complete your account setup</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="margin: 0 0 20px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Hello,
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Thank you for signing up with <strong>HireNest Team Platform</strong>! We're excited to have you on board.
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                To complete your registration and start using your account, please verify your email address by clicking the button below:
                            </p>

                            <!-- Email Display Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8f9fa; border-left: 4px solid #667eea; border-radius: 6px; margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 8px 0; color: #6c757d; font-size: 13px; font-weight: 500;">Your Email Address:</p>
                                        <p style="margin: 0; color: #212529; font-size: 16px; font-weight: 600;">{email}</p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Verify Button -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 30px;">
                                <tr>
                                    <td align="center" style="padding: 10px 0;">
                                        <a href="{url}" style="display: inline-block; padding: 16px 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #ffffff; text-decoration: none; font-weight: 600; font-size: 16px; border-radius: 8px; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">Verify Email Address</a>
                                    </td>
                                </tr>
                            </table>

                            <!-- Alternative Link -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8f9fa; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #495057; font-size: 14px; font-weight: 600;">
                                            Button not working?
                                        </p>
                                        <p style="margin: 0 0 10px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            Copy and paste this link into your browser:
                                        </p>
                                        <p style="margin: 0; word-break: break-all;">
                                            <a href="{url}" style="color: #667eea; font-size: 13px; text-decoration: none;">{url}</a>
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Info Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 15px 20px;">
                                        <p style="margin: 0; color: #856404; font-size: 13px; line-height: 1.6;">
                                            <strong>⏱️ Important:</strong> This verification link will expire in 24 hours for security purposes. If you didn't create an account with us, please ignore this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                Once verified, you'll have full access to all features of HireNest Team Platform. If you have any questions, feel free to reach out to our support team.
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <p style="margin: 0 0 10px 0; color: #667eea; font-weight: 600; font-size: 18px;">HireNest Team Platform</p>
                                        <p style="margin: 0 0 15px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            © 2026 HireNest Team. All rights reserved.<br>
                                            Building better experiences together.
                                        </p>
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tr>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Privacy Policy</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Terms of Service</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Support</a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="margin: 15px 0 0 0; color: #adb5bd; font-size: 12px;">
                                            123 Business Street, Suite 100, City, State 12345<br>
                                            This is an automated message. Please do not reply to this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                </table>

                <!-- Mobile-only text -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 20px auto 0;">
                    <tr>
                        <td align="center" style="color: #999999; font-size: 12px; padding: 0 20px;">
                            You received this email because you created an account with HireNest Team Platform.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""
    
    result = {
        "subject": subject,
        "body": body
    }
    return result


def company_details_uploaded():
    subject = "Thank You - Details Uploaded Successfully"

    
    body = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Company Details Uploaded Successfully</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <div style="width: 80px; height: 80px; background-color: rgba(255,255,255,0.2); border-radius: 50%; display: inline-block; text-align: center; line-height: 80px; margin-bottom: 20px;">
                                            <span style="font-size: 45px; color: #ffffff;">✓</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 28px; font-weight: 600;">Details Uploaded Successfully!</h1>
                                        <p style="margin: 0; color: #ffffff; font-size: 16px; opacity: 0.95;">Thank you for joining us</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="margin: 0 0 20px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Dear Partner,
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                <strong>Thank you for joining HireNest Platform!</strong> We're excited to have you as part of our growing community.
                            </p>
                            <p style="margin: 0 0 30px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Your company details have been uploaded successfully and are now under review by our team.
                            </p>

                            <!-- Success Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #d4edda; border-left: 4px solid #28a745; border-radius: 6px; margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #155724; font-size: 15px; font-weight: 600;">
                                            ✅ Submission Complete
                                        </p>
                                        <p style="margin: 0; color: #155724; font-size: 14px; line-height: 1.6;">
                                            Your company information has been received and is being processed by our verification team.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- What's Next Section -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 25px;">
                                <tr>
                                    <td>
                                        <h2 style="margin: 0 0 20px 0; color: #333333; font-size: 20px; font-weight: 600;">What Happens Next?</h2>
                                    </td>
                                </tr>
                            </table>

                            <!-- Steps -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 15px 0; border-bottom: 1px solid #e9ecef;">
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="40" valign="top">
                                                    <div style="width: 30px; height: 30px; background-color: #667eea; border-radius: 50%; color: #ffffff; text-align: center; line-height: 30px; font-weight: 600; font-size: 14px;">1</div>
                                                </td>
                                                <td valign="top">
                                                    <p style="margin: 0 0 5px 0; color: #333333; font-size: 15px; font-weight: 600;">Review Process</p>
                                                    <p style="margin: 0; color: #6c757d; font-size: 14px; line-height: 1.5;">Our team will carefully review your submitted information and documents.</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 15px 0; border-bottom: 1px solid #e9ecef;">
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="40" valign="top">
                                                    <div style="width: 30px; height: 30px; background-color: #667eea; border-radius: 50%; color: #ffffff; text-align: center; line-height: 30px; font-weight: 600; font-size: 14px;">2</div>
                                                </td>
                                                <td valign="top">
                                                    <p style="margin: 0 0 5px 0; color: #333333; font-size: 15px; font-weight: 600;">Verification</p>
                                                    <p style="margin: 0; color: #6c757d; font-size: 14px; line-height: 1.5;">We'll verify all details to ensure compliance and accuracy.</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 15px 0;">
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="40" valign="top">
                                                    <div style="width: 30px; height: 30px; background-color: #667eea; border-radius: 50%; color: #ffffff; text-align: center; line-height: 30px; font-weight: 600; font-size: 14px;">3</div>
                                                </td>
                                                <td valign="top">
                                                    <p style="margin: 0 0 5px 0; color: #333333; font-size: 15px; font-weight: 600;">Notification</p>
                                                    <p style="margin: 0; color: #6c757d; font-size: 14px; line-height: 1.5;">Our team will inform you via email once the verification is complete.</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>

                            <!-- Info Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #e7f3ff; border-left: 4px solid #0066cc; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #004085; font-size: 14px; font-weight: 600;">
                                            ⏱️ Expected Timeline
                                        </p>
                                        <p style="margin: 0; color: #004085; font-size: 14px; line-height: 1.6;">
                                            Our verification process typically takes 2-3 business days. You'll receive an email notification as soon as your account is approved and ready to use.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <p style="margin: 0 0 20px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                In the meantime, feel free to explore our platform or reach out to our support team if you have any questions.
                            </p>

                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                We appreciate your patience and look forward to working with you!
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <p style="margin: 0 0 10px 0; color: #667eea; font-weight: 600; font-size: 18px;">HireNest Platform</p>
                                        <p style="margin: 0 0 15px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            © 2026 HireNest. All rights reserved.<br>
                                            Building better partnerships together.
                                        </p>
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tr>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Privacy Policy</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Terms of Service</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Support</a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="margin: 15px 0 0 0; color: #adb5bd; font-size: 12px;">
                                            123 Business Street, Suite 100, City, State 12345<br>
                                            This is an automated message. Please do not reply to this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                </table>

                <!-- Mobile-only text -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 20px auto 0;">
                    <tr>
                        <td align="center" style="color: #999999; font-size: 12px; padding: 0 20px;">
                            You received this email because you submitted company details to HireNest Platform.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""

    result = {
    "subject": subject,
    "body": body
    }
    
    return result

def company_approved(name, time):
    # Professional Subject Line
    subject = f"Dear {name}, your company is approved by HireNest"
    
    # HTML Body with a modern, corporate aesthetic
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #f4f7f9;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }}
            .email-wrapper {{
                width: 100%;
                background-color: #f4f7f9;
                padding: 40px 0;
            }}
            .content-card {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }}
            .status-banner {{
                background-color: #00c853; /* Success Green */
                color: #ffffff;
                padding: 30px;
                text-align: center;
            }}
            .main-body {{
                padding: 40px;
                color: #2c3e50;
                line-height: 1.8;
            }}
            .company-name {{
                font-size: 22px;
                color: #1a73e8;
                font-weight: bold;
            }}
            .timestamp {{
                display: inline-block;
                background: #f1f3f4;
                padding: 5px 12px;
                border-radius: 4px;
                font-size: 13px;
                margin-top: 10px;
            }}
            .footer {{
                padding: 20px;
                text-align: center;
                font-size: 12px;
                color: #95a5a6;
            }}
            .btn {{
                display: inline-block;
                padding: 12px 25px;
                background-color: #1a73e8;
                color: #ffffff;
                text-decoration: none;
                border-radius: 6px;
                font-weight: bold;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="email-wrapper">
            <div class="content-card">
                <div class="status-banner">
                    <h1 style="margin:0;">Verification Approved</h1>
                </div>
                <div class="main-body">
                    <p>Dear <span class="company-name">{name}</span>,</p>
                    
                    <p>We are pleased to inform you that your profile has been successfully 
                    <strong>verified</strong> and <strong>approved</strong> by the HireNest administration team.</p>
                    
                    <p>Our platform has reviewed your credentials and confirmed your company's 
                    eligibility to connect with our network of professionals.</p>

                    <div class="timestamp">
                        Approved on: {time}
                    </div>

                    <p style="margin-top: 30px;">You can now start posting job vacancies, searching for candidates, 
                    and building your employer brand immediately.</p>
                    
                    <a href="https://hirenest.com/login" class="btn">Access Your Dashboard</a>

                    <p style="margin-top: 40px;">Best regards,<br>
                    <strong>The HireNest Verification Team</strong></p>
                </div>
                <div class="footer">
                    &copy; 2026 HireNest Platform. All rights reserved.<br>
                    If you did not request this, please ignore this email.
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    result = {
    "subject": subject,
    "body": body
    }
    
    return result



def reject_company(name, time, reason):
    # Professional Subject Line
    subject = f"Update regarding your company verification on HireNest"
    
    # HTML Body with a professional, clear layout
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #f4f7f9;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }}
            .email-wrapper {{
                width: 100%;
                background-color: #f4f7f9;
                padding: 40px 0;
            }}
            .content-card {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }}
            .status-banner {{
                background-color: #ff9800; /* Warning Orange */
                color: #ffffff;
                padding: 30px;
                text-align: center;
            }}
            .main-body {{
                padding: 40px;
                color: #2c3e50;
                line-height: 1.8;
            }}
            .company-name {{
                font-size: 20px;
                color: #d32f2f;
                font-weight: bold;
            }}
            .reason-box {{
                background-color: #fff3e0;
                border-left: 4px solid #ff9800;
                padding: 20px;
                margin: 20px 0;
                font-style: italic;
                color: #e65100;
            }}
            .footer {{
                padding: 20px;
                text-align: center;
                font-size: 12px;
                color: #95a5a6;
            }}
            .contact-link {{
                color: #1a73e8;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="email-wrapper">
            <div class="content-card">
                <div class="status-banner">
                    <h1 style="margin:0;">Verification Update</h1>
                </div>
                <div class="main-body">
                    <p>Dear <span class="company-name">{name}</span>,</p>
                    
                    <p>Thank you for your interest in joining the HireNest platform. Our administration team has completed the review of your company profile submitted on <strong>{time}</strong>.</p>
                    
                    <p>At this time, we are <strong>unable to approve</strong> your company account due to the following reason:</p>
                    
                    <div class="reason-box">
                        "{reason}"
                    </div>

                    <p>If you believe this was an error, or if you can provide the missing information, please log in to your dashboard to update your details or reach out to our support team.</p>
                    
                    <p style="margin-top: 40px;">Best regards,<br>
                    <strong>The HireNest Compliance Team</strong></p>
                    
                    <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                    <p style="font-size: 13px;">Questions? Visit our <a href="#" class="contact-link">Help Center</a> or contact support.</p>
                </div>
                <div class="footer">
                    &copy; 2026 HireNest Platform. All rights reserved.
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    result = {
    "subject": subject,
    "body": body
    }

    return result




def resume_shortlisted(name, company_name, time):

    subject = f"Great news, {name}! Your resume was shortlisted by {company_name}"
    
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #f0f4f8;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }}
            .email-wrapper {{
                width: 100%;
                background-color: #f0f4f8;
                padding: 40px 0;
            }}
            .content-card {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 16px;
                overflow: hidden;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            }}
            .status-banner {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #ffffff;
                padding: 40px 20px;
                text-align: center;
            }}
            .main-body {{
                padding: 40px;
                color: #2d3748;
                line-height: 1.8;
            }}
            .highlight-text {{
                color: #5a67d8;
                font-weight: bold;
                font-size: 18px;
            }}
            .info-badge {{
                display: inline-block;
                background: #ebf4ff;
                color: #2b6cb0;
                padding: 8px 16px;
                border-radius: 50px;
                font-size: 14px;
                font-weight: 600;
                margin: 15px 0;
            }}
            .next-steps {{
                background-color: #f7fafc;
                border-radius: 8px;
                padding: 20px;
                margin-top: 25px;
                border: 1px dashed #cbd5e0;
            }}
            .footer {{
                padding: 25px;
                text-align: center;
                font-size: 12px;
                color: #a0aec0;
            }}
        </style>
    </head>
    <body>
        <div class="email-wrapper">
            <div class="content-card">
                <div class="status-banner">
                    <h1 style="margin:0; font-size: 28px;">Congratulations!</h1>
                    <p style="margin: 10px 0 0 0; opacity: 0.9;">You've been shortlisted</p>
                </div>
                <div class="main-body">
                    <p>Hi <strong>{name}</strong>,</p>
                    
                    <p>We have exciting news! Your resume has been reviewed and <span class="highlight-text">shortlisted</span> by the hiring team at <strong>{company_name}</strong>.</p>
                    
                    <div class="info-badge">
                        Shortlisted on: {time}
                    </div>

                    <div class="next-steps">
                        <h4 style="margin-top:0; color: #4a5568;">What happens next?</h4>
                        <p style="margin-bottom:0;">The team from <strong>{company_name}</strong> will contact you very soon via your registered email or phone number to discuss the next steps in the interview process.</p>
                    </div>

                    <p style="margin-top: 30px; text-align: center; font-style: italic; color: #4a5568;">
                        Keep your phone nearby and your inbox open. Best of luck with your upcoming interview!
                    </p>
                    
                    <p style="margin-top: 40px;">Best regards,<br>
                    <strong>The HireNest Team</strong></p>
                </div>
                <div class="footer">
                    &copy; 2026 HireNest | Connecting Talent with Opportunity.<br>
                    You received this because your profile is active on HireNest.
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    result = {
    "subject": subject,
    "body": body
    }

    return result
    
    return subject, body
# Example usage:
# email_body = company_details_uploaded()
# send_email(to=company_email, subject="Thank You - Details Uploaded Successfully", body=email_body)